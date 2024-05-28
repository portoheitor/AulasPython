import sqlite3
from CREATE_ import DB_FILE, TABLE_NAME

connection = sqlite3.connect(database=DB_FILE)
cursor = connection.cursor()

if __name__ == '__main__':

    """INSERIR DADOS NA TABELA"""

    # name = 'Leonardo di Caraprius'
    # weigth = 5.5
    # sql_ = (f'INSERT INTO {TABLE_NAME} (name, weight) '
    #         f'VALUES("{name}","{weigth}")')
    #
    # cursor.execute(sql_)
    # connection.commit()

    """INSERINDO DADOS POR DICIONARIOS"""

    nomes = [{'name': 'Heitor', 'weight': 8.8},
             {'name': 'Jose', 'weight': 8.0},
             {'name': 'Ariell', 'weight': 8.3},
             {'name': 'Lourds', 'weight': 100.00},
             {'name': 'snake', 'weight': 4.5}, ]

    sql_ = (f'INSERT INTO {TABLE_NAME} (name, weight) '
            f'VALUES(:name,:weight)')

    #se VALUES(? : ?) tem que desempacotar os nomes
    #nomes_to_insert = [(item['name'], item['weight']) for item in nomes]

    connection.executemany(sql_, nomes)

    """VISUALIZAR DADOS / CAMPOS"""

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )
    connection.commit()

    for row in cursor.fetchall():
        _id, name, weigth = row
        print(_id, name, weigth)

    cursor.close()
    connection.close()
