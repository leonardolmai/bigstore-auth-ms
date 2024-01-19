from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.presentation.composers.company.get_company_by_cnpj_composer import (
    get_company_by_cnpj_composer,
)


def get_current_company(
    x_company_cnpj: Annotated[str, Header()],
    session: Session = Depends(get_db),
):
    current_company = get_company_by_cnpj_composer(session, x_company_cnpj)
    if current_company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid company CNPJ"
        )

    return current_company
