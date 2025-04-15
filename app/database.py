from sqlmodel import create_engine
from sqlmodel import SQLModel

engine = create_engine("postgresql+psycopg2://app:password@db/app")
#                       driver://user:password@host/db
# CF: sharemycode.fr/27c

def init_database():
    SQLModel.metadata.create_all(engine)