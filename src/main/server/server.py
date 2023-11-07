from fastapi import FastAPI

from src.presentation.routers import (
    company_routers,
    token_routers,
    user_routers,
)

app = FastAPI()

app.include_router(user_routers.router)
app.include_router(token_routers.router)
app.include_router(company_routers.router)
