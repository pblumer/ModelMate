import click
from src.model.graph import (
    add_application,
    get_applications,
    add_business_capability,
    get_business_capabilities,
    add_relationship,
)

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
@click.option("--description", default="", help="Description of the application.")
def add_app(name, description):
    """Add a new application to the graph."""
    add_application(name, description)
    click.echo(f"Added application: {name}")

@cli.command()
def list_apps():
    """List all applications in the graph."""
    apps = get_applications()
    if apps:
        for app in apps:
            click.echo(app)
    else:
        click.echo("No applications found.")

@cli.command()
@click.argument("name")
@click.option("--description", default="", help="Description of the business capability.")
def add_capability(name, description):
    """Add a new business capability to the graph."""
    add_business_capability(name, description)
    click.echo(f"Added business capability: {name}")

@cli.command()
def list_capabilities():
    """List all business capabilities in the graph."""
    capabilities = get_business_capabilities()
    if capabilities:
        for cap in capabilities:
            click.echo(cap)
    else:
        click.echo("No business capabilities found.")

@cli.command()
@click.argument("source")
@click.argument("target")
@click.argument("relation_type")
def add_relation(source, target, relation_type):
    """Add a relationship between two entities."""
    add_relationship(source, target, relation_type)
    click.echo(f"Added relationship: {source} --{relation_type}--> {target}")

@cli.command()
@click.argument("source")
@click.argument("target")
@click.argument("relation_type")
def remove_relation(source, target, relation_type):
    """Remove a relationship between two entities."""
    # Implement removal logic if needed
    click.echo(f"Removed relationship: {source} --{relation_type}--> {target}")
