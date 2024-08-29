import sqlite3
import typer

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS creds(
    id integer PRIMARY KEY,
    name TEXT,
    accesskey TEXT,
    secretkey TEXT,
    region TEXT,
    bucket_name TEXT
    ) '''
    cursor.execute(query)
    conn.commit()
    return conn, cursor

def insert(configName: str, accesskey: str, secretkey: str, region: str, bucket_name: str | None):
    query = f'''
    INSERT INTO users (name,accesskey,secretkey, region,bucket_name) VALUES ({configName}, {accesskey}, {secretkey}, {region}, {bucket_name})
    '''
    conn, cursor = init_db()
    try:
        conn, cursor = init_db()
        cursor.execute(query)
        conn.commit()
        typer.secho("Credential Saved Successfully!", fg=typer.colors.GREEN)
    except:
        typer.secho("Failed to Save credentials!", fg=typer.colors.RED)
    conn.close()

def get_all_configs():
    conn, cursor = init_db()
    query = '''
    SELECT * from creds
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows
