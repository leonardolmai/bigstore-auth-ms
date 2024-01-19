from fastapi import HTTPException, status
from jose import JWTError, jwt

from src.domain.use_cases.user.get_user import GetUserUseCaseInterface
from src.main.settings.config import settings
from src.presentation.schemas.token import TokenData
from src.presentation.schemas.user import UserOut


class GetAuthenticatedUserController:
    def __init__(self, use_case: GetUserUseCaseInterface) -> None:
        self.__use_case = use_case

    def handle(self, token) -> UserOut | None:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError as exc:
            raise credentials_exception from exc
        response = self.__use_case.execute(token_data.username)
        if response is None:
            raise credentials_exception
        return response
