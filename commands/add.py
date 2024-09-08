import typer
from database.database import insert
from database.profile import list_profiles
from helpers.helpers import enc_input
import click
import os
import hashlib
from datetime import datetime


addApp = typer.Typer()

@addApp.command()
def config():
    if not list_profiles():
        typer.secho("Error: No Profile Found, Create One First!!", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    
    configType = int(typer.prompt("Choose a credential type\n  (1)general\n  (2)s3\n", type = click.Choice(['1', '2']), show_choices=False));
    listedTypes = [1,2]
    if configType not in listedTypes:
        typer.secho("Error: Please Proceed with the listed type!")
    configName = typer.prompt("Assign a Name for this credential")
    if configName.strip() == '':
        typer.secho("Error: A name is must", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    attr = '' 
    _configType= ''
    if configType == 2:
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
        attr = {
            'name' :configName,
            'secretkey':secretKey,
            'accesskey':accessKey,
            'region':region,
            'bucketname':bucketName
        }
        _configType = 's3'
    elif configType == 1:
        uname = typer.prompt("Enter Username/Email")
        if not uname:
            typer.secho("Error: Please Enter Username/Email", fg=typer.colors.RED)
        pwd = typer.prompt("Enter Password")
        if not pwd:
            typer.secho("Error: Please Enter Password", fg=typer.colors.RED)
        pwd = enc_input(pwd)
        attr = {
            'username':uname,
            'password':pwd
        }
        _configType = 'general'
    enc_text = enc_input(str(attr))
    now = datetime.now()
    created_at = now.strftime("%d/%m/%Y %H:%M:%S")
    if insert(_configType, configName, enc_text,created_at):
        typer.secho("Credential Saved Successfully!!", fg=typer.colors.GREEN)
    else:
        typer.secho("Failed to Save credentials!!", fg=typer.colors.RED)
if __name__ == "__main__":
    addApp()
