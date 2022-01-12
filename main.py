from sqlite import inserir, login
from db_pass import delete, insert, list_passwords
import projeto_senhas as ps
from time import sleep


def main() -> None:
    new_user = int(input('If you are a new user, type 3. Else type any other number: '))
    if new_user == 3:
        inserir()
        menu()
    else:
        name = input('Insert your user: ')
        passwrd = input('Insert your password: ')
        login(name, passwrd)
        menu()


def menu() -> None:
    print('****************************************')
    print('=Welcome to gen/admin password generator=')
    print('****************************************')

    print('Select what you want to do: ')
    print('1 - generate a new password')
    print('2 - check your passwords')
    print('3 - remove a password(s)')

    option: int = int(input())

    if option == 1:
        val = ps.generatepass()
        insert(val)
        sleep(5)
        menu()
    elif option == 2:
        list_passwords()
        sleep(5)
        novo_menu = input('Do you want to make another process? ')
        if novo_menu == 'y' or novo_menu == 'yes':
            menu()
        else:
            exit()
    elif option == 3:
        delete()
        sleep(5)
        novo_menu = input('Do you want to make another process? ')
        if novo_menu == 'y' or novo_menu == 'yes':
            menu()
        else:
            exit()


#if __name__ == '__main__':
main()