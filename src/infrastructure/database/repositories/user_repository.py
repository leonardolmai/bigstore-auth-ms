from typing import Any

from sqlalchemy.orm import Session

from src.data.repositories.user_repository import UserRepositoryInterface
from src.domain.entities.user import User
from src.infrastructure.database.models.user import User as UserModel


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def list_users(self) -> list[User] | None:
        try:
            return self.session.query(UserModel).all()
        except:
            return None

    def get_user(self, email: str) -> User | None:
        try:
            return (
                self.session.query(UserModel)
                .filter(UserModel.email == email)
                .one_or_none()
            )
        except:
            return None

    def create_user(self, user: User) -> User | None:
        try:
            user_data = {
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "phone": user.phone,
                "cpf": user.cpf,
            }
            user_model = UserModel(**user_data)

            self.session.add(user_model)
            self.session.commit()

            return user_model
        except:
            return None

    def update_user(self, email: str, update_fields: dict[str, Any]) -> User | None:
        try:
            self.session.query(UserModel).filter(UserModel.email == email).update(
                update_fields
            )
            self.session.commit()
            user_updated = self.get_user(email)

            return user_updated
        except:
            return None

    def delete_user(self, email: str) -> bool:
        try:
            self.session.query(UserModel).filter(UserModel.email == email).update(
                {UserModel.is_active: False}
            )
            self.session.commit()
            return True
        except:
            return False
