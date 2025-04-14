"""
Make a connection to the SQLITE database.
"""

from dotenv import load_dotenv
import os
from sqlmodel import Session, create_engine, SQLModel
from src.model import models

load_dotenv()

sqlite_url = os.getenv("SQLITE_URL") 
conn_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, connect_args=conn_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
