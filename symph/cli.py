import click

from .server import run_server


@click.group(name="symph")
def symph():
    """FastAPI webserver to orchestrate Celery workflows."""
    pass


@symph.command()
@click.option(
    "--broker-url",
    "-b",
    required=True,
    help="The url to the message broker, e.g redis://1.2.3.4",
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

    server_kwargs = {"broker_url": broker_url, "port": port}

    run_server(**server_kwargs)
