import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

""" CRUD -> Create Read   Update Delete
    SQL -> INSERT SELECT UPDATE DELETE """
if __name__ == '__main__':
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    """CRIAR TABELA """
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
        f'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        f'name TEXT, '
        f'weight REAL)'
    )

    connection.commit()

    cursor.close()
    connection.close()

"""
COMANDO PARA EXCLUIR A TABELA :
-> cursor.execute(f'DROP TABLE {TABLE_NAME}')

COMANDO PARA EXCLUIR O BANCO DE DADOS
-> cursor.execute(f'DROP DATABASE {DATA_BASE}')
"""
