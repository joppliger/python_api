from os import getenv
from typing import Annotated
from pydantic import BaseModel
from pydantic import Field
from fastapi import APIRouter
from fastapi import Depends
from api.v1.models import Quote

apiv1 = APIRouter(prefix="/api/v1")

class GetVersionResponse(BaseModel):
    version: str

@apiv1.get("/version")
def get_version() -> GetVersionResponse:
    """This route return the current version of the api"""
    version = getenv("VERSION", "0.0.0")
    return GetVersionResponse(version=version)

class SayHelloBody(BaseModel):
    name: Annotated[str, Field(min_length=1)]

@apiv1.get("/hello")
def say_hello(body: SayHelloBody) -> str:
    return f"Hello {body.name}"

names = [
    "bob",
    "alice",
    "carole",
    "denise",
    "edgar",
    "fanfan",
    "gérard",
    "hyperlegend"
]

class Paging(BaseModel):
    limit: int = 10
    offset: int = 0

PagingDeps = Annotated[Paging, Depends()]

@apiv1.get("/name/all")
def get_all_names(paging: PagingDeps) -> list:
    return names[paging.offset:paging.offset+paging.limit]

@apiv1.post("/quote")
def insert_quote(quote: Quote) -> Quote:
    return quote