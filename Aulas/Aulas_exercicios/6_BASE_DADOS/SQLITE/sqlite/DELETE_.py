# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE
import sqlite3
from CREATE_ import DB_FILE, TABLE_NAME

if __name__ == '__main__':
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        # deletar_id = 1
        # cursor.execute(
        #     f'DELETE FROM {TABLE_NAME} WHERE id={deletar_id}'
        # )
        #
        # connection.commit()

        cursor.execute(
            f'DELETE FROM {TABLE_NAME} WHERE id BETWEEN 14 AND (SELECT MAX(id) FROM {TABLE_NAME});'
        )
        connection.commit()




        """VISUALIZAR DADOS / CAMPOS"""

        cursor.execute(
            f'SELECT * FROM {TABLE_NAME}'
        )
        connection.commit()

        for row in cursor.fetchall():
            print(*row)

        cursor.close()
        connection.close()

    except Exception as error:
        print(f"Ocorreu um erro durante o delete: {error}")
