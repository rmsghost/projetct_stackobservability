import mysql.connector
import csv

# cursor = conexao.cursor()
# cursor.execute("SELECT * FROM clientes")
# resultados = cursor.fetchall()
# cursor.execute("INSERT INTO clientes (nome, email) VALUES ('João', 'joao@email.com')")
# cursor.execute("UPDATE clientes SET nome = 'Pedro' WHERE id = 1")

# cursor.execute("SELECT * FROM clientes")
# resultados = cursor.fetchall()

# cursor.execute("DELETE FROM clientes WHERE id = 1")

def addPokemon():
    connection = None
    try:
        print(f'Tentando conexão com o banco..')
        connexao = mysql.connector.connect(
        host='bd-pkm',
        user='root',
        password='123@123',
        database='padrao'
        )
        print(f'Conectado!')
    except Exception as erro:
        print(f'Erro de conexão: {erro}')

    cursor = connexao.cursor()
    print(f'lendo CSV')
    my_data = []
    with open('pokemon.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            my_data.append(tuple(row))
    print(my_data)
    query = 'INSERT INTO padrao.POKEMON_INFO(id_pokedex, name_pokemon) VALUES (%s, %s)'
    cursor.executemany(query,my_data)

    connexao.commit()
    cursor.close()
    connexao.close()


def consultPokemon(id_pokedex):
    connection = None
    try:
        print(f'Tentando conexão com o banco..')
        connexao = mysql.connector.connect(
        host='bd-pkm',
        user='root',
        password='123@123',
        database='padrao'
        )
        print(f'Conectado!')
    except Exception as erro:
        print(f'Erro de conexão: {erro}')
    
    cursor = connexao.cursor()
    
    query = f"SELECT * FROM POKEMON_INFO where id_pokedex = {id_pokedex}"
    cursor.execute(query)
    resultados = cursor.fetchall()

    print(type(resultados))
    print(resultados[0])

    connexao.commit()
    cursor.close()
    connexao.close()

    return resultados

def allPokemon():
    connection = None
    try:
        print(f'Tentando conexão com o banco..')
        connexao = mysql.connector.connect(
        host='bd-pkm',
        user='root',
        password='123@123',
        database='padrao'
        )
        print(f'Conectado!')
    except Exception as erro:
        print(f'Erro de conexão: {erro}')
    
    cursor = connexao.cursor()
    
    query = f"SELECT * FROM POKEMON_INFO"
    cursor.execute(query)
    resultados = cursor.fetchall()

    print(type(resultados))
    print(resultados[2])

    connexao.commit()
    cursor.close()
    connexao.close()

    return resultados