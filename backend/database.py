import os
import ssl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Environment se URL fetch karein
DATABASE_URL = os.getenv("DATABASE_URL")

# --- AIVEN DATABASE SSL FIX ---
# Aiven ko SSL chahiye, par hum certificate verify bypass karenge
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
# ------------------------------

# 2. Engine banayein aur custom SSL pass karein
engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": ssl_context}  # Yeh line jaadu karegi!
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()