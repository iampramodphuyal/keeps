import sqlite3

DATABASE_NAME = 'keeps.db'
DATABASE_TABLE = 'creds'


def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = f'''CREATE TABLE IF NOT EXISTS {DATABASE_TABLE}(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
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
    query = f"""
    INSERT INTO {DATABASE_TABLE} (name,accesskey,secretkey, region,bucket_name) VALUES ('{configName}', '{accesskey}', '{secretkey}', '{region}', '{bucket_name}');
    """
    print(f"query :: {query}")
    try:
        conn, cursor = init_db()
        cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def get_all_configs():
    conn, cursor = init_db()
    query = '''
    SELECT * from creds
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

