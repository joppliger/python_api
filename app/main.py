from fastapi import FastAPI
from dotenv import load_dotenv
from api.v1 import apiv1

load_dotenv()

app = FastAPI()

app.include_router(apiv1)
