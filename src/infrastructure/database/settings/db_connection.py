from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.models.base import Base
from src.main.settings.config import settings

DB_URL = settings.DATABASE_URL

engine = create_engine(DB_URL)

Base.metadata.create_all(engine)


SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
