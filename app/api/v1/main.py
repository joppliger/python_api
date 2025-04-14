from os import getenv
from typing import Annotated
from pydantic import BaseModel
from pydantic import Field
from fastapi import APIRouter

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
