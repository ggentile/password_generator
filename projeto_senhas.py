import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' , 'v',
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V' , 'X',
'W', 'Y', 'Z']

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


symbols_list = ['!', '?', '#', '$', '%', '&', '*']


final_password = []
def generatepass():
     print("Welcome to the PyPassword Generator!")

     letters = int(input("How many letters would you like in your password?\n"))
     symbols = int(input("How many symbols would you like?\n"))
     numbers = int(input("How many numbers would you like?\n"))

     for char in range(0, letters + 1): 
          x = random.choice(letters_list)
          final_password.append(x)

     for sy in range(0, symbols + 1):
          x = random.choice(symbols_list)
          final_password.append(x)

     for sy in range(0, numbers + 1):
          x = random.choice(numbers_list)
          final_password.append(x)


     random.shuffle(final_password)


     new_pass = ''.join(map(str, final_password))

     print(new_pass)
     encriptado = new_pass
     return encriptado

