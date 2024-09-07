import typer
from database.database import insert
from database.profile import list_profiles

addApp = typer.Typer()

@addApp.command()
def config():
    if not list_profiles():
        typer.secho("Error: No Profile Found, Create One First!!", fg=typer.colors.RED)
        raise typer.Exit(code=1)
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
    if insert(configName, secretKey, accessKey, region, bucketName):
        typer.secho("Credential Saved Successfully!", fg=typer.colors.GREEN)
    else:
        typer.secho("Failed to Save credentials!", fg=typer.colors.RED)

if __name__ == "__main__":
    addApp()
