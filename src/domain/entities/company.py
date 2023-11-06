class Company:
    def __init__(
        self,
        id: int,
        name: str,
        cnpj: str,
        owner_id: int,
        website: str | None = None,
        is_approved: bool = False,
        is_active: bool = True,
    ) -> None:
        self.id = id
        self.name = name
        self.cnpj = cnpj
        self.owner_id = owner_id
        self.website = website
        self.is_approved = is_approved
        self.is_active = is_active
