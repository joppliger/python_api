from typing import Annotated
from sqlmodel import create_engine
from sqlmodel import SQLModel
from sqlmodel import Session
from fastapi import Depends

engine = create_engine("postgresql+psycopg2://app:password@db/app")
#                       driver://user:password@host/db
# CF: sharemycode.fr/27c

def init_database():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDeps = Annotated[Session, Depends(get_session)]