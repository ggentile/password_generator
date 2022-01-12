import sqlite3


def connectar():

    conn1 = sqlite3.connect('users.db')
    conn1.execute(""" CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        password TEXT NOT NULL);""")

    return conn1

def desconectar(conn):

    conn.close()

def login(user, password):
    conn = connectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM usuarios WHERE nome = '{user}' AND password = '{password}'")
    usr = cursor.fetchall()

    if len(usr) > 0:
       print(usr)
    else:
        print('user not found.')

    desconectar(conn)

#for now, leave this function for tests:
def list():
    conn = connectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usr = cursor.fetchall()

    if len(usr) > 0:
        for user in usr:
            print(f'ID: {usr[0]}')
            print(f'NOME: {usr[1]}')
            print(f'PASSWORD: {usr[2]}')
    else:
        print('No users yet.')
    desconectar(conn)

def inserir():
    
    conn = connectar()
    cursor = conn.cursor()

    nome = input('Inform the name of the new user: ')
    password = input('Informe the new password: ')

    cursor.execute(f"INSERT INTO usuarios (nome, password) VALUES ('{nome}', '{password}')")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'{nome} was saved')
    else: 
        print('An error has ocurred')

    desconectar(conn)

def atualizar():
    
    conn = connectar()
    cursor = conn.cursor()

    id = int(input('Inform the ID of the user: '))
    nome = input('Inform the name of the user: ')
    password = input('Inform the password of the user: ')

    cursor.execute(f"UPDATE usuarios SET nome = '{nome}', password = '{password}' WHERE ID = '{id}'")
    conn.commit()

    if cursor.rowcount == 1:
        print('The alterations were saved')
    else:
        print('An error has occurred')

    desconectar(conn)

def deletar():
    conn = connectar()
    cursor = conn.cursor()

    id = int(input('Insert the id of user you wish to DELETE: '))

    cursor.execute(f"DELETE FROM usuarios WHERE id='{id}'")
    conn.commit()

    if cursor.rowcount == 1:
        print('Information deleted successfully')
    else:
        print('An error has ocurred')

    desconectar(conn)

