import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight)'
    'VALUES (:nome, :peso)'
)
# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(
#     sql,
#     (
#         ('Joana', 4), ('Luiz', 5)
#     )
# )

lista_customers = (
    {'nome': 'Larissa', 'peso': 3},
    {'nome': 'Erci', 'peso': 2},
    {'nome': 'Romanele', 'peso': 4},
    {'nome': 'Derci', 'peso': 5},
)

# cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
cursor.executemany(sql, lista_customers)
connection.commit()

cursor.close()
connection.close()
"""
# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()
"""

if __name__ == '__main__':
    ...