import typer
from database.profile import create,list_profiles, check_profile


profileApp = typer.Typer()

@profileApp.command()
def create_profile():
    username = typer.prompt("Username")
    if check_profile(username):
        typer.secho(f"Username{username} Already Exists! Create new one", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    password = typer.prompt("Password(min length 4)", hide_input=True)
    if not password:
        typer.secho(f"Password Empty, enter a valid one", fg=typer.colors.RED)
    if len(password) < 4:
        typer.secho(f"Password not of valid length, enter a valid one", fg=typer.colors.RED)

    verifypwd = typer.prompt("Verify Password", hide_input=True)
    if not verifypwd:
        typer.secho(f"Verify Password Empty, enter a valid one", fg=typer.colors.RED)
    if password != verifypwd:
        typer.secho(f"Password donot match", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    hint = typer.prompt("Password Hint")


@profileApp.command()
def login():
    pass
