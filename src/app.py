from fastapi import FastAPI
from src.api.routes import user

app = FastAPI()

app.include_router(user.router)
