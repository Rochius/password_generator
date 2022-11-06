import random
import os

capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

numbers = [1,2,3,4,5,6,7,8,9,0]

passwords_and_apps = {}


def obligatory_characters():
    obl_chars = []
    obl_chars.append(random.choice(capital_letters))
    obl_chars.append(random.choice(capital_letters).lower())
    obl_chars.append(str(random.choice(numbers)))
    return obl_chars

def desorer_list (char_list, password_length):
    char_list = random.sample(char_list, (password_length + 3))
    char_list_joined = ''.join(char_list)
    return char_list_joined

def generate_password(key):
    char_type = [1,2,3]
    password_length = random.randint(9,16) - 3
    char_list = obligatory_characters()
    for index in range(0,password_length):
        character_option = random.choice(char_type)
        if character_option == 1:
            character = random.choice(capital_letters)
        elif character_option == 2:
            character = random.choice(capital_letters).lower()
        elif character_option == 3:
            character = str(random.choice(numbers))
        char_list.append(character)
    final_password = desorer_list(char_list, password_length)
    passwords_and_apps[key]= final_password


def menu():
    b = True
    user_name = input('Please, enter your name: ')
    while b:
        os.system("cls")
        print(f'Hi {user_name}!!')
        print(' 1) Generate Password\n 2) Show passwprds \n 0) Exit')
        op = input('Please, select an option (1, 2, 0): ')
        if op == '1':
            pass
        elif op == '2':
            pass
        elif op == '0':
            pass
        else:
            print("That is not an available option, please try again")
        

menu()