import factory
from factory import Faker
from sqlalchemy import orm

from src.infrastructure.database.models.company import Company
from src.infrastructure.database.models.user import User

Session = orm.scoped_session(orm.sessionmaker())


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = Session

    name = Faker("name")
    email = Faker("email")
    password = Faker("password")
    phone = Faker("phone_number")
    cpf = Faker("numerify")
    is_active = Faker("boolean")


class CompanyFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Company
        sqlalchemy_session = Session

    name = Faker("name")
    cnpj = Faker("numerify")
    website = Faker("url")
    owner = factory.SubFactory(UserFactory)
    is_approved = Faker("boolean")
    is_active = Faker("boolean")
