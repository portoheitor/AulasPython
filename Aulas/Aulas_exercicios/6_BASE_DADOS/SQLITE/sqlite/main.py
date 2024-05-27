import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
BD_NAME = 'db.sqlite3'
BD_FILE = ROOT_DIR / BD_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(BD_FILE)
cursor = connection.cursor()

#CRIAR TABELA
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'wight REAL'
    ')'
)

connection.commit()

cursor.close()
connection.close()
