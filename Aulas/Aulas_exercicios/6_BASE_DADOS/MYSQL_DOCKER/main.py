# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

if __name__ == '__main__':
    try:
        """CRIANDO CONEXAO COM SERVIDOR"""
        connection = pymysql.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['YSQL_DATABASE'],
            charset='utf8mb4'
        )

        """CRIANDO TABELA"""
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS customers ('
                    'id INT NOT NULL AUTO_INCREMENT, '
                    'name VARCHAR(50) NOT NULL, '
                    'age INT NOT NULL, '
                    'PRIMARY KEY (id)'
                    ')'
                )
                connection.commit()

                """INSERINDO DADOS NA TABELA"""
                with connection.cursor() as cursor:
                    sql = (
                        f'INSERT INTO customers (name, age) '
                        f'VALUES (%s, %s) '
                    )
                    data = ('Maite', 1)
                    cursor.execute(sql, data)
                connection.commit()

                #inserindo dicionario
                with connection.cursor() as cursor:
                    sql = (
                        f'INSERT INTO customers (name, age) '                        
                        f'VALUES (%(name)s, %(age)s '
                    )
                    data2 = {
                        "name": "Heitor",
                        "age": 30,
                    }
                    cursor.execute(sql, data2)
                connection.commit()

    except Exception as error:
        print(f'Ocorreu um erro durante a consulta SQL {error}')
        raise error
