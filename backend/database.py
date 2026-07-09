import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def _build_engine():
    if DATABASE_URL:
        return create_engine(DATABASE_URL)

    sqlite_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hcp_crm.db"))
    return create_engine(f"sqlite:///{sqlite_path}", connect_args={"check_same_thread": False})


engine = _build_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()