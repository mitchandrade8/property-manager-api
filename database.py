import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Load the variables from the .env file
load_dotenv()

# 2. Securely grab the URL from the environment
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 3. Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()