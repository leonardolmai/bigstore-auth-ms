from datetime import datetime, timedelta

from fastapi import HTTPException, status
from jose import jwt

from src.main.settings.config import pwd_context, settings
from src.presentation.schemas.token import TokenOut


class AuthenticateUserUserController:
    def handle(self, user, form_data) -> TokenOut | None:
        user = self.__authenticate_user(user, form_data.password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.__create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        response = {"access_token": access_token, "token_type": "bearer"}

        return response

    def __authenticate_user(self, user, password: str):
        if not user:
            return False
        if not self.__verify_password(password, user.password):
            return False
        return user

    def __create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return encoded_jwt

    def __verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
