# pylint: disable=unused-argument
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.main.settings.config import oauth2_scheme
from src.presentation.composers.user.create_user_composer import create_user_composer
from src.presentation.composers.user.delete_user_composer import delete_user_composer
from src.presentation.composers.user.get_authenticated_user_composer import (
    get_authenticated_user_composer,
)
from src.presentation.composers.user.list_users_composer import list_users_composer
from src.presentation.composers.user.update_user_composer import update_user_composer
from src.presentation.schemas.user import UserCreate, UserOut, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def list_users(
    token: Annotated[str, Depends(oauth2_scheme)],
    x_company_cnpj: Annotated[str, Header()],
    session: Session = Depends(get_db),
):
    user: UserOut = get_authenticated_user_composer(session, token)
    users = list_users_composer(session)
    if users:
        return [user]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")


@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    x_company_cnpj: Annotated[str, Header()],
    session: Session = Depends(get_db),
):
    user = get_authenticated_user_composer(session, token)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(
    user: UserCreate,
    x_company_cnpj: Annotated[str, Header()],
    session: Session = Depends(get_db),
):
    user = create_user_composer(session, user)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail="User already exists."
    )


@router.patch("/{email}", status_code=status.HTTP_200_OK, response_model=UserOut)
def update_user(
    email: str,
    user: UserUpdate,
    x_company_cnpj: Annotated[str, Header()],
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_db),
):
    user = user.model_dump(exclude_unset=True)
    current_user = get_authenticated_user_composer(session, token)
    if current_user:
        user = update_user_composer(session, email, user)
        if user:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    x_company_cnpj: Annotated[str, Header()],
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Session = Depends(get_db),
):
    user = get_authenticated_user_composer(session, token)
    user = delete_user_composer(session, user.email)
    if user:
        return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
