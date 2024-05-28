import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, wigth = row
    print(_id, name, wigth)

print()

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id="6"')

row = cursor.fetchone()
_id, name, wigth =row
print(_id, name,wigth)

cursor.close()
connection.close()
