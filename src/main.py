from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.v1.api import api_router

fastapi_app = FastAPI(
    title="Symph",
    description="FastAPI webserver to orchestrate workflows on Celery workers",
)

fastapi_app.include_router(api_router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000",
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "*",
]

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)