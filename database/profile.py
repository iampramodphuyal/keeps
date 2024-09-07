
import sqlite3

DATABASE_NAME = 'keeps.db'
DATABASE_TABLE = 'profile'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    query = f'''CREATE TABLE IF NOT EXISTS {DATABASE_TABLE}(
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        pwdHint TEXT,
        isDefault TEXT,
        created_at TEXT NOT NULL,
        modified_at TEXT
        ); '''
    cursor.execute(query)
    conn.commit()
    return conn, cursor

def create_profile(username, password, hint, default, created_at):
    query = f"""
    INSERT INTO {DATABASE_TABLE} (username, password, pwdHint, isDefault, created_at) VALUES ('{username}', '{password}', '{hint}', '{default}', '{created_at}');
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
    SELECT username, password,isDefault FROM {DATABASE_TABLE} WHERE username='{username}'
    '''
    try:
        conn, cursor = init_db()
        cursor.execute(query)
        rows = dict(cursor.fetchone())
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


