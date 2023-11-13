class UserCompany:
    def __init__(
        self,
        id: int,
        user_id: int,
        company_id: int,
        is_employee: bool = False,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.company_id = company_id
        self.is_employee = is_employee
