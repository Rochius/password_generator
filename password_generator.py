import random

capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

numbers = [1,2,3,4,5,6,7,8,9,0]

value_options = [1,2,3]

password_length = random.randint(8,16) - 3
password = ""
password_array = []

password_array.append(random.choice(capital_letters))
password_array.append(random.choice(capital_letters).lower())
password_array.append(str(random.choice(numbers)))

for index in range(0,password_length):
    character_option = random.choice(value_options)
    if character_option == 1:
        character = random.choice(capital_letters)
    elif character_option == 2:
        character = random.choice(capital_letters).lower()
    elif character_option == 3:
        character = str(random.choice(numbers))
    
    password_array.append(character)


password_array = random.sample(password_array, (password_length + 3))
password = "".join(password_array)

print(password)
