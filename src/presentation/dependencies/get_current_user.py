from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.infrastructure.database.settings.db_connection import get_db
from src.main.settings.config import oauth2_scheme
from src.presentation.composers.user.get_authenticated_user_composer import (
    get_authenticated_user_composer,
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_db),
):
    current_user = get_authenticated_user_composer(session, token)
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    return current_user
