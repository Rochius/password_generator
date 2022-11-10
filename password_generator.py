import random
import os
import msvcrt

capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

numbers = [1,2,3,4,5,6,7,8,9,0]

passwords_and_apps = {}

FILE_NAME = 'Passwords.txt'

def pause_system():
    print("\nPress a key to continue...")
    msvcrt.getch()

#GENERATE PASSWORD
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

def generate_password():
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
    # passwords_and_apps[key]= final_password
    # print(f'\nYour {key} password is: {passwords_and_apps[key]}')
    # print('Password succefully added!!')
    return final_password




def change_to_string(password , app_name):
    passwords_in_string = f'{app_name}: {password}\n'
    return passwords_in_string

def app_exists(app_name):
    with open(FILE_NAME, 'r') as file:
        for line in file:
            words = line.split(': ')
            if app_name.lower() == words[0].lower():
                return True
    return False

def store_passwords(password, app_name):
    file = open(FILE_NAME, 'a')
    file.write(change_to_string(password , app_name))
    file.close()
    print('Succefully stored')


def show_passwords():
    with open(FILE_NAME , 'r') as file:
        for line in file:
            print(line)

def replace_passwords(password, app_name):
    with open(FILE_NAME, 'r') as file:
        x = file.read()
    lines = x.split('\n')
    for i in range(0, len(lines)):
        if app_name.lower() in lines[i].lower():
            lines[i] = change_to_string(password, app_name).rstrip()
    x = '\n'.join(lines)

    with open(FILE_NAME , 'w') as file:
        file.write(x)

def file_is_empty():
    with open(FILE_NAME, 'r') as file:
        file.seek(0, os.SEEK_END)
        isempty = file.tell() == 0
        file.seek(0)
        return isempty

def menu():
    b = True
    user_name = input('Please, enter your name: ')

    while b:
        os.system("cls")
        print(f'Hi {user_name}!!')
        print(' 1) Generate Password\n 2) Show passwords \n 0) Exit')
        op = input('Please, select an option (1, 2, 0): ')

        if op == '1':
            app_name = input('Please, indicate which app the password will be for: ')
            if app_exists(app_name):
                generate_option = input(f'You already have a {app_name} password, Do you want to overwrite it? (y/n): ')
                
                if generate_option.lower() == 'y':
                    password = generate_password()
                    replace_passwords(password , app_name)
                    pause_system()
                elif generate_option.lower() != 'y' and generate_option.lower() != 'n':
                    print('That is not an available option...')
                    pause_system()
            else:
                password = generate_password()
                store_passwords(password , app_name)
                pause_system()

        elif op == '2':
            if not file_is_empty():
                print('\nThis are your passwords:')
                show_passwords()
                pause_system()
            else:
                print('\nYou do not have any passwords...')
                pause_system()

        elif op == '0':
            print('Thank you for use our system!!')
            b = False
        else:
            print("That is not an available option, please try again")
            pause_system()
        



menu()


