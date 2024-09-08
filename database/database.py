import sqlite3

DATABASE_NAME = 'keeps.db'
DATABASE_TABLE = 'creds'


def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = f'''CREATE TABLE IF NOT EXISTS {DATABASE_TABLE}(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    configType TEXT NOT NULL,
    enc_text TEXT NOT NULL,
    profile_id integer NOT NULL,
    created_at TEXT NOT NULL,
    modified_at TEXT 
    ) '''
    cursor.execute(query)
    conn.commit()
    return conn, cursor

def insert(configType:str, configName:str, enc_text:str):
    query = f"""
    INSERT INTO {DATABASE_TABLE} (name,configType, enc_text, created_at, profile_id) VALUES ('{configName}', '{configType}', '{enc_text}', '{created_at}', '{profile_id}');
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

