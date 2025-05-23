import click
from flask.cli import AppGroup
from . import db  # Assuming db is in app's __init__.py
from .models import User  # Assuming User model is in app/models.py

user_cli = AppGroup('user')

@user_cli.command('create-admin')
@click.argument('username')
@click.argument('password')
def create_admin_command(username, password):
    """Creates a new admin user."""
    if User.query.filter_by(username=username).first():
        click.echo(f'User {username} already exists.')
        return
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    click.echo(f'Admin user {username} created successfully.')

def register_commands(app):
    """Registers CLI commands with the Flask app."""
    app.cli.add_command(user_cli)
