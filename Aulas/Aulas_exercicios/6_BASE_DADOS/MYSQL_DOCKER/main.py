# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
from dotenv import load_dotenv
import pymysql
import pymysql.cursors

load_dotenv()

if __name__ == '__main__':
    try:
        """CRIANDO CONEXAO COM SERVIDOR"""
        connection = pymysql.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['YSQL_DATABASE'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
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
                #LIMPANDO TABELA PARA AULA CUIADO AO USAR TRUNCATE NO DIA A DIA#
                cursor.execute('TRUNCATE TABLE customers')
                connection.commit()
                #####################################################################

                """INSERINDO DADOS NA TABELA C"""
                print('INSERINDO DADOS ->')
                with connection.cursor() as cursor:
                    sql = (
                        'INSERT INTO customers(name, age) VALUES(%s, %s)'
                    )
                    data = ('Jose', 30)
                    cursor.execute(sql, data)
                    connection.commit()

                #inserindo dicionario ou pode ser tupla
                with connection.cursor() as cursor:
                    sql2 = (
                        'INSERT INTO customers(name, age) VALUES(%(name)s, %(age)s)'
                    )
                    data2 = {
                        "name": "Joaozinho",
                        "age": 55,
                    }
                    cursor.execute(sql2, data2)
                    connection.commit()

                #inserindo varios valores em 1 so chamda
                with connection.cursor() as cursor:
                    sql3 = (
                        'INSERT INTO customers(name, age) VALUES(%(name)s, %(age)s)'
                    )
                    data3 = (
                        {"name": "Pedrinho", "age": 5, },
                        {"name": "Carlota", "age": 35, },
                        {"name": "Paulina", "age": 46, },
                        {"name": "Bred Pitu", "age": 58, },
                    )
                    cursor.executemany(sql3, data3)
                    connection.commit()

                #####################################################################
                print('SELECIONANDO/CAPTURANDO DADOS ->')
                """LENDO/CPTURANDO DADOS DA TABELA"""
                with connection.cursor() as cursor:
                    sql_select = (
                        'SELECT id, name, age FROM customers'
                    )  # ou uso SELECT * para tudo
                    cursor.execute(sql_select)

                    result_select = cursor.fetchall()
                    #todos dados ou fetcone() = um valor

                    for row in result_select:
                        print(row)

                    print('#*#' *15 )

                #FILTRANDO AS BUSCAS
                with connection.cursor() as cursor:
                    sql_select1 = (
                        'SELECT * FROM customers WHERE id BETWEEN %s AND %s'
                    )  # > < <> >= <= BETWEEN(ENTRE)
                    cursor.execute(sql_select1, (2, 5))
                    result_select1 = cursor.fetchall()
                    for row in result_select1:
                        print(row)

                    print('#->' * 15)
                #####################################################################
                print('FAZENDO UPDADTE NOS DADOS ->')
                """ FAZENDO UPDADE NOS DADOS"""
                with connection.cursor() as cursor:
                    sql_update = (
                        'UPDATE customers SET name=%s, age=%s WHERE id=%s '
                    )
                    cursor.execute(sql_update, ("Louro jose", 55, 4))
                    connection.commit()

                    cursor.execute('SELECT * FROM customers')
                    for row in cursor.fetchall():
                        print(row)
                    print('#->' * 15)

                #####################################################################
                print('DELETANDO DADOS ->')
                """FAZENDO DELETE NOS DADOS"""
                with connection.cursor() as cursor:
                    sql_delete = (
                        'DELETE FROM customers WHERE id = %s'
                    )
                    cursor.execute(sql_delete, 4)

                    connection.commit()

                    cursor.execute('SELECT * FROM customers')
                    for row in cursor.fetchall():
                        print(row)
                    print('#->' * 15)

                    """RESETANDO O SCROLL PARA CONSEGUIR FAZER OUTRO FOUR
                        SEM TER QUE ARMAZENAR EM UMA VARIAVEL NO SISTEMA
                        EM CASOS DE GRANDES BANCOS VOCE ESTOURARIA O PC
                    """
                    print('Scrol resetado')
                    cursor.scroll(0, 'absolute')
                    for row in cursor.fetchall():
                        print(row)

                #####################################################################

    except Exception as error:
        print(f'Ocorreu um erro durante a consulta SQL {error}')
        raise error
