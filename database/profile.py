
import sqlite3

DATABASE_NAME = 'creds.db'
DATABASE_TABLE = 'profile'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = f'''CREATE TABLE IF NOT EXISTS {DATABASE_TABLE}(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT,
    password TEXT,
    hint TEXT,
    default TEXT,
    created_at TEXT,
    modified_at TEXT
    ) '''
    cursor.execute(query)
    conn.commit()
    return conn, cursor

def create_profile(username, password, hint, default, created_at):
    query = f"""
    INSERT INTO {DATABASE_TABLE} (username, password, hint, default, created_at) VALUES ('{username}', '{password}', '{hint}', '{default}', '{created_at}');
    """
    try:
        conn, cursor = init_db()
        cursor.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def list_profiles():
    query = f'''
    SELECT username, default FROM {DATABASE_TABLE}
    '''
    try:
        conn, cursor = init_db()
        cursor.execute(query)
        rows = cursor.fetchall() 
        conn.close()
        return rows
    except:
        return False

def check_profile(username:str):
    query = f'''
    SELECT {username}, password FROM {DATABASE_TABLE}
    '''
    try:
        conn, cursor = init_db()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except:
        return False

def login(username:str, password:str):
    query = f'''
    SELECT {username}, {password} FROM {DATABASE_TABLE}
    '''
    try:
        conn, cursor = init_db()
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            print(row)
            pass
    except:
        return False


