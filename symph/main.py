from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from symph.routers.v1.api import api_router

app = FastAPI(
    title="Symph",
    description="FastAPI webserver to orchestrate workflows on Celery workers",
)

app.include_router(api_router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000",
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# if __name__ == "__main__":
#     uvicorn.run("symph.main:app", host="0.0.0.0", port=8000)
