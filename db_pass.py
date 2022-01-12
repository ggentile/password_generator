import sqlite3


def connectar():

    conn1 = sqlite3.connect('passwords.db')
    conn1.execute(""" CREATE TABLE IF NOT EXISTS minhas_senhas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        empresa_usado TEXT NOT NULL,
        password TEXT NOT NULL);""")

    return conn1

def desconectar(conn):

    conn.close()

#def login(user, password):
    '''conn = connectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM minhas_senhas WHERE nome = '{user}' AND password = '{real_password}'")
    usr = cursor.fetchall()

    if len(usr) > 0:
       print(usr)
    else:
        print('user not found.')

    desconectar(conn)
'''
#for now, leave this function for tests:
def list_passwords():
    conn = connectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM minhas_senhas')
    usr = cursor.fetchall()

    if len(usr) > 0:
        for user in usr:
            print(f'Senhas: {user}')
    else:
        print('No users yet.')
    desconectar(conn)

def insert(passwrd):
    conn = connectar()
    cursor = conn.cursor()

    nome = input('Insert your name: ')
    empresa = input('Inform where you registered your password: ')
    cursor.execute(f"INSERT INTO minhas_senhas (nome, empresa_usado, password) VALUES ('{nome}', '{empresa}', '{passwrd}')")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'{nome} was saved')
    else: 
        print('An error has ocurred')

    desconectar(conn)

def delete():
    conn = connectar()
    cursor = conn.cursor()

    list()
    id = int(input('Insert the id of password you wish to DELETE: '))

    cursor.execute(f"DELETE FROM minhas_senhas WHERE id='{id}'")
    conn.commit()

    if cursor.rowcount == 1:
        print('Information deleted successfully')
    else:
        print('An error has ocurred')

    desconectar(conn)

