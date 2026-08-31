from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.database_url,
    echo=True,
) if settings.database_url else None


SessionLocal = (
    sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )
    if engine
    else None
)


def get_db():
    if SessionLocal is None:
        raise RuntimeError("DATABASE_URL is not configured")

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()