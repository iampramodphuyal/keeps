import typer
from commands.add import addApp
from commands.profile import profileApp

app = typer.Typer()
app.add_typer(addApp, name="add", help="Add new s3 config to store")
app.add_typer(profileApp, name="profile", help="Add profile to store passwords")

if __name__ == "__main__":
    app()
