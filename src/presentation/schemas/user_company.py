from pydantic import BaseModel

from src.presentation.schemas.user import UserOut


class UserCompanyCreate(BaseModel):
    user_id: int
    company_id: int
    is_employee: bool | None = None


class UserCompanyUpdate(BaseModel):
    user_id: int | None = None
    company_id: int | None = None
    is_employee: bool | None = None


class UserCompanyOut(BaseModel):
    id: int
    user: UserOut
    company_id: int
    is_employee: bool | None
