import click
import uvicorn
from celery import Celery
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from symph.routers import deps
from symph.routers.v1.api import api_router


@click.group(name="symph")
def cli():
    """FastAPI webserver to orchestrate Celery workflows."""
    pass


@cli.command()
@click.option(
    "--broker-url",
    "-b",
    required=True,
    help="The url to the broker, e.g redis://1.2.3.4",
)
@click.option(
    "--port",
    "-p",
    required=True,
    type=int,
    help="The port that Symph runs on, e.g 8000",
)
def run(broker_url, port):
    """Run FastAPI webserver"""

    async def on_startup() -> None:
        celery_app = Celery(broker=broker_url)
        app.dependency_overrides[deps.get_celery_app] = lambda: celery_app

    app = FastAPI(
        title="Symph",
        description="FastAPI webserver to orchestrate workflows on Celery workers",
        on_startup=[on_startup],
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

    uvicorn.run(app, host="0.0.0.0", port=port)
