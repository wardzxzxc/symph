from pathlib import Path

import uvicorn
from celery import Celery
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kombu import exceptions as kombu_exc
from watchgod import run_process

from symph.routers import deps
from symph.routers.v1.api import api_router


def _create_server(broker_url: str) -> FastAPI:
    def on_startup() -> None:
        celery_app = Celery(broker=broker_url)
        try:
            celery_app.control.ping()
        except kombu_exc.OperationalError:
            raise ValueError("broker_url is incorrect")

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

    return app


def run_server(broker_url: str, port: int):
    app = _create_server(broker_url)
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":  # pragma: no cover
    # solely for dev purpose
    import argparse

    parser = argparse.ArgumentParser(description="Launch a development server")
    parser.add_argument(
        "-b", "--broker_url", help="The url to the message broker, e.g redis://1.2.3.4"
    )
    parser.add_argument(
        "-p", "--port", help="The port that dev server runs on, e.g 8000", type=int
    )

    args = parser.parse_args()

    server_kwargs = {"broker_url": args.broker_url, "port": args.port}

    run_process(path=(Path.cwd()).absolute(), target=run_server, kwargs=server_kwargs)
