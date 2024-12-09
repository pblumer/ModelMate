import click
from model.graph import add_application, get_applications

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
def add_app(name):
    """Add a new application to the graph."""
    add_application(name)
    click.echo(f"Added application: {name}")

@cli.command()
def list_apps():
    """List all applications in the graph."""
    apps = get_applications()
    for app in apps:
        click.echo(app)
