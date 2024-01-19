from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.user.authenticate_user_composer import (
    authenticate_user_composer,
)
from src.presentation.schemas.token import TokenOut

router = APIRouter(prefix="/token", tags=["token"])


@router.post("/", status_code=status.HTTP_200_OK, response_model=TokenOut)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    x_company_cnpj: Annotated[str | None, Header()] = None,
    session: Session = Depends(get_db),
):
    token = authenticate_user_composer(session, form_data, x_company_cnpj)
    if token:
        return token
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Problem generating token."
    )
