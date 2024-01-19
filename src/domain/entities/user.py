class User:
    def __init__(
        self,
        id: int,
        name: str,
        email: str,
        password: str,
        phone: str | None = None,
        cpf: str | None = None,
        is_active: bool = True,
    ) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.cpf = cpf
        self.is_active = is_active
