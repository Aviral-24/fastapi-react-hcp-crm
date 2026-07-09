import os
import ssl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Fetch URL from Render
raw_url = os.getenv("DATABASE_URL", "")

# --- ULTIMATE FIX: URL ko force-clean karein ---
# Agar URL ke end mein koi bhi ?ssl_disabled ya kuch aur juda hai, 
# toh yeh code usko kaat kar URL ko bilkul pure bana dega.
if "?" in raw_url:
    DATABASE_URL = raw_url.split("?")[0]
else:
    DATABASE_URL = raw_url

# 2. Force SSL without checking certificate (Aiven bypass)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 3. Apply Engine
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