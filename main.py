import typer
from commands.add import addApp


app = typer.Typer()
app.add_typer(addApp, name="add", help="Add new s3 config to store")

if __name__ == "__main__":
    app()
