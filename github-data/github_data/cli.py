import click
from github_data.api import get_data

@click.command()
@click.argument("username")
def main(username):
    """Fetch Github user data"""
    try:
        data = get_data(username)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1)
    
    click.echo(f"Username : {data['login']}")
    click.echo(f"Name : {data.get('name')}")
    click.echo(f"Repos : {data['public_repos']}")
    click.echo(f"Followers : {data['followers']}")
    click.echo(f"Following : {data['following']}")
