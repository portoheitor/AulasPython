from CREATE_ import DB_FILE, TABLE_NAME
import sqlite3

if __name__ == '__main__':
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        """ATUALIZANDO VALORES"""

        novo_nome = "Pretorios Suspicios"
        novo_weight = 11.11
        id_alterar = 1
        cursor.execute(f'UPDATE {TABLE_NAME} '
                       f'SET name = "{novo_nome}", weight = {novo_weight} '
                       f'WHERE id={id_alterar}')
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