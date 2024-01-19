from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str | None = None
    cpf: str | None = None


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    phone: str | None = None
    cpf: str | None = None
    is_active: bool | None = None


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None
    cpf: str | None
    is_active: bool
