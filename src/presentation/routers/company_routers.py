# pylint: disable=unused-argument
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.company.create_company_composer import (
    create_company_composer,
)
from src.presentation.composers.company.delete_company_composer import (
    delete_company_composer,
)
from src.presentation.composers.company.get_company_composer import get_company_composer
from src.presentation.composers.company.list_companies_composer import (
    list_companies_composer,
)
from src.presentation.composers.company.update_company_composer import (
    update_company_composer,
)
from src.presentation.composers.user_company.create_user_company_composer import (
    create_user_company_composer,
)
from src.presentation.composers.user_company.delete_user_company_composer import (
    delete_user_company_composer,
)
from src.presentation.composers.user_company.list_user_companies_composer import (
    list_user_companies_composer,
)
from src.presentation.dependencies.get_current_company import get_current_company
from src.presentation.dependencies.get_current_user import get_current_user
from src.presentation.schemas.company import CompanyCreate, CompanyOut, CompanyUpdate
from src.presentation.schemas.user import UserOut
from src.presentation.schemas.user_company import UserCompanyOut

router = APIRouter(prefix="/companies", tags=["companies"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CompanyOut])
def list_companies(
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    # current_company: CompanyOut = Depends(get_current_company),
    session: Session = Depends(get_db),
):
    if current_user:
        companies = list_companies_composer(session)
        if companies:
            return companies
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Companies not found."
    )


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CompanyOut)
def get_company(
    id: int,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_user:
        company = get_company_composer(session, id)
        if company:
            return company
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Company not found."
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompanyOut)
def create_company(
    company: CompanyCreate,
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
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
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if company.website:
        company.website = jsonable_encoder(company.website)
    company = company.model_dump(exclude_unset=True)
    if current_user:
        company = update_company_composer(session, id, company)
        if company:
            return company
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Company not found."
    )


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(
    x_company_cnpj: Annotated[str, Header()],
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_user:
        company = delete_company_composer(session, current_user.company.id)
    if company:
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Company not found."
    )


@router.get(
    "/employees/",
    status_code=status.HTTP_200_OK,
    response_model=list[UserCompanyOut],
    tags=["employees"],
)
async def list_employees(
    x_company_cnpj: Annotated[str, Header()],
    current_company: CompanyOut = Depends(get_current_company),
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_company:
        employees = list_user_companies_composer(session, current_user, current_company)
        return employees
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Employees not found."
    )


@router.post(
    "/employees/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserCompanyOut,
    tags=["employees"],
)
def add_employee(
    email: str,
    x_company_cnpj: Annotated[str, Header()],
    current_company: CompanyOut = Depends(get_current_company),
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_company:
        employee = create_user_company_composer(session, current_company, email)
        if employee:
            return employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found."
    )


@router.delete(
    "/employees/",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["employees"],
)
def remove_employee(
    email: str,
    x_company_cnpj: Annotated[str, Header()],
    current_company: CompanyOut = Depends(get_current_company),
    current_user: UserOut = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    if current_company:
        employee = delete_user_company_composer(session, current_company, email)
        if employee:
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found."
    )
