from fastapi import FastAPI
from dotenv import load_dotenv
from api.v1 import apiv1
from database import init_database

load_dotenv()
init_database()

app = FastAPI()

app.include_router(apiv1)
