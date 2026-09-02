from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# The URL for creating the database
DATABASE_URL = "postgresql+psycopg2://david:686462@localhost:5432/expense-tracker-db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for creating tables using python classes
class Base(DeclarativeBase):
    pass