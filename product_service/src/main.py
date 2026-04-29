from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Product Service")

app.include_router(router)