from pydantic import AnyUrl, BaseModel


class CompanyCreate(BaseModel):
    name: str
    cnpj: str
    website: AnyUrl | None = None


class CompanyUpdate(BaseModel):
    name: str | None = None
    cnpj: str | None = None
    website: AnyUrl | None = None
    is_approved: bool | None = None
    is_active: bool | None = None


class CompanyOut(BaseModel):
    id: int
    name: str
    cnpj: str
    website: str | None
    owner_id: int
    is_active: bool
    is_approved: bool
