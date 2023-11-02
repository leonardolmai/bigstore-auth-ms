from fastapi import FastAPI

from src.presentation.routers import token_routers, user_routers

app = FastAPI()

app.include_router(user_routers.router)
app.include_router(token_routers.router)
