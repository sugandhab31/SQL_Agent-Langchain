import requests
import pathlib
import sqlite3
from contextlib import contextmanager

def load_db():
    url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"
    local_path = pathlib.Path("chinook.db")

    if local_path.exists():
        print(f"{local_path} already exists, skipping downloading.")
    else:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            local_path.write_bytes(response.content)
            print(f"Successfully downloaded {url} to {local_path}")
            return local_path
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
            return None

@contextmanager
def connect_db(local_db_path: str):
    con = sqlite3.connect(local_db_path)
    try:
        yield con
    finally:
        con.close()

    """cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall() if not row[0].startswith("sqlite_")]

    print("Dialect: sqlite")
    print(f"Available tables: {tables}")

    cursor.execute("SELECT * FROM Artist LIMIT 5;")
    print(f"Sample output: {cursor.fetchall()}")
    con.close()"""