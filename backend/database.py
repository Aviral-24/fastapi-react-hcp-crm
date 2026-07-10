import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Render seedha humari URL uthayega bina kisi ched-chad ke
DATABASE_URL = os.getenv("DATABASE_URL")

# Engine create karein (pool_pre_ping connection drop hone se bachata hai)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()