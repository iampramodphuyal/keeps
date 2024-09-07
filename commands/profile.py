import typer
from database.profile import create_profile,list_profiles, check_profile
import hashlib
import os
from datetime import datetime

profileApp = typer.Typer()

@profileApp.command()
def create():
    username = typer.prompt("Username")
    check = check_profile(username)
    print(check)
    if check:
        typer.secho(f"Username: `{username}` Already Exists! Create New One!!", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    password = typer.prompt("Password(min length 4)", hide_input=True)
    if not password:
        typer.secho(f"Password Empty, Enter a Valid One", fg=typer.colors.RED)
    if len(password) < 4:
        typer.secho(f"Password not of valid length, Enter a Valid One", fg=typer.colors.RED)

    verifypwd = typer.prompt("Verify Password", hide_input=True)
    if not verifypwd:
        typer.secho(f"Verify Password Empty, Enter a Valid One", fg=typer.colors.RED)
    if password != verifypwd:
        typer.secho(f"Password Donot Match", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    salt = os.urandom(32)
    password = hashlib.pbkdf2_hmac('sha-256', password.encode('utf-8'), salt, 100000)
    hashPwd = (salt+password).hex()
    hint = typer.prompt("Password Hint")
    default = 'Yes'
    now = datetime.now()
    created_at = now.strftime("%d/%m/%Y %H:%M:%S")
    if create_profile(username, hashPwd, hint, default,created_at):
        typer.secho(f"Username: {username} Added as Default Successfully!", fg=typer.colors.GREEN)
    else:
        typer.secho(f"Username: {username} Faild to save!", fg=typer.colors.RED)


@profileApp.command()
def login():
    username = typer.prompt("Username")
    if check_profile(username):
        password = typer.prompt("Password", hide_input=True)
        pass
    else:
        typer.secho(f"Username{username} Not Found!", fg=typer.colors.RED)
        raise typer.Exit(code=1)
