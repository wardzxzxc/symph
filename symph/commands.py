import click


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
    help="The port that Symph runs on, e.g 8000",
)
def run(broker_url, port):
    """Run FastAPI webserver"""
    click.echo(broker_url)
    click.echo(port)
    click.echo("Initialized the database")
