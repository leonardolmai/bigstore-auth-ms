from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic_settings import BaseSettings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    COMPANY_CNPJ: str
    ALLOWED_ORIGINS: str

    class Config:
        env_file = ".env"


settings = Settings()
