import typer
from database.database import insert

addApp = typer.Typer()

@addApp.command()
def config():
    configName = typer.prompt("Assign a Name for this credential")
    if not configName.strip():
        typer.secho("Error: A name is must", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    accessKey = typer.prompt("Enter AccessKey")
    if not accessKey.strip():
        typer.secho("Error: Accesskey is empty", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    secretKey = typer.prompt("Enter SecretKey")
    if not secretKey.strip():
        typer.secho("Error: SecretKey is empty", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    region = typer.prompt("Enter Region(eu-central-1)", default="eu-central-1")
    bucketName = typer.prompt("Enter Bucket Name", default=None)
    insert(configName, secretKey, accessKey, region, bucketName)

if __name__ == "__main__":
    addApp()
