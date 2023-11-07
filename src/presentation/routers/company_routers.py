from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.main.settings.config import oauth2_scheme
from src.presentation.composers.create_company_composer import (
    create_company_composer,
)
from src.presentation.composers.delete_company_composer import (
    delete_company_composer,
)
from src.presentation.composers.get_authenticated_user_composer import (
    get_authenticated_user_composer,
)
from src.presentation.composers.get_company_composer import (
    get_company_composer,
)
from src.presentation.composers.list_companies_composer import (
    list_companies_composer,
)
from src.presentation.composers.update_company_composer import (
    update_company_composer,
)
from src.presentation.schemas.company import (
    CompanyCreate,
    CompanyOut,
    CompanyUpdate,
)

router = APIRouter(prefix="/companies", tags=["companies"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CompanyOut])
def list_companies(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_db),
):
    user: CompanyOut = get_authenticated_user_composer(session, token)
    if user:
        companies = list_companies_composer(session)
        if companies:
            return companies
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Companies not found."
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CompanyOut)
def get_company(
    id: int,
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_db),
):
    user = get_authenticated_user_composer(session, token)
    if user:
        company = get_company_composer(session, id)
        if company:
            return company
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Company not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompanyOut)
def create_company(
    company: CompanyCreate,
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_db),
):
    current_user = get_authenticated_user_composer(session, token)
    company.website = jsonable_encoder(company.website)
    if current_user:
        company = create_company_composer(session, company, current_user.id)
        if company:
            return company
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="Company already exists."
    )


@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=CompanyOut)
def update_company(
    id: int,
    company: CompanyUpdate,
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_db),
):
    if company.website:
        company.website = jsonable_encoder(company.website)
    company = company.model_dump(exclude_unset=True)
    current_user = get_authenticated_user_composer(session, token)
    if current_user:
        company = update_company_composer(session, id, company)
        if company:
            return company
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Company not found."
    )


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_db),
):
    current_user = get_authenticated_user_composer(session, token)
    if current_user:
        company = delete_company_composer(session, current_user.company.id)
    if company:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Company not found."
    )
