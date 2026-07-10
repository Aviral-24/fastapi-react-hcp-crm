import os
import ssl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. URL fetch karein
raw_url = os.getenv("DATABASE_URL", "")

# 2. URL Force-Clean (Agar purana ?ssl_disabled juda ho toh use hatayein)
if "?" in raw_url:
    DATABASE_URL = raw_url.split("?")[0]
else:
    DATABASE_URL = raw_url

# 3. Aiven Bypass SSL Context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 4. Engine with strict SSL dict
engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": ssl_context}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()