from sqlmodel import SQLModel
from sqlmodel import Field

class Quote(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True)
    author: str
    content: str

