import random

# Lists with leters and numbers to extract elements randomly
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

numbers = [1,2,3,4,5,6,7,8,9,0]

# These values ​​represent if the array will enter numbers, uppercase or lowercase 
value_options = [1,2,3]

password_length = random.randint(9,16) - 3 # This will be the length of the password not counting the 3 mandatory characters
password = ""
password_list = []

password_list.append(random.choice(capital_letters)) # The obligatory capital letter
password_list.append(random.choice(capital_letters).lower()) # The obligatory lower letter
password_list.append(str(random.choice(numbers))) # The obligatory number

# This for cicle will add a random number, capital letter or lower letter to the password list
for index in range(0,password_length):
    character_option = random.choice(value_options)
    if character_option == 1:
        character = random.choice(capital_letters)
    elif character_option == 2:
        character = random.choice(capital_letters).lower()
    elif character_option == 3:
        character = str(random.choice(numbers))
    
    password_list.append(character)


password_list = random.sample(password_list, (password_length + 3))
password = "".join(password_list)

print(password)
