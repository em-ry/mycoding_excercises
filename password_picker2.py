# PASSWORD GENERATOR

import random
import string


def custom_pwd()->"password":
    """Collects data and generates passwords"""
    while True:
        adjectives = input("Input a list of comma seperated adjectives: ").split(",")
        nouns = input("Input a list of comma seperated nouns: ").split(",")

        num = input("How many passwords should be generated? ")
        for i in range(int(num)):
            adjective = random.choice(adjectives)
            noun = random.choice(nouns)
            number = random.randrange(0,100)
            special_char = random.choice(string.punctuation)#brings out all the special characters

            order = input("Choose the order of password:\n 1) adj,noun,num,sym \n 2)num,adj,sym,noun \n 3) sym,noun,num,adj \n Answer: ")
            if order == '1':
                password = adjective + noun + str(number) + special_char
                print('Your new password is %s' %password)
            elif order == '2':
                password = str(number)+ adjective + special_char + noun
                print('Your new password is %s' %password)
            elif order == '3':
                password =  special_char + noun + str(number) + adjective
                print('Your new password is %s' %password)

        print('\n')
        response = input('Would you like another password? Type y or n: ')
        if response == 'n':
            print('Memorize your passord! GOODBYE!!!')
            break



    
def default_pwd():
    """Uses default data and generates password"""
    while True:
        adjectives = ['sleepy', 'slow', 'smelly',
                          'wet', 'fat', 'red', 'orange',
                          'yellow', 'green', 'blue', 'purple',
                          'fluffy', 'white', 'proud', 'brave']

        nouns = ['apple', 'dinosaur', 'ball',
                    'toaster', 'goat', 'dragon',
                    'hammer', 'duck', 'panda']

        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0,100)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + str(number) + special_char
        print('Your new password is %s' %password)
            
        print('\n')
        response = input('Would you like another password? Type y or n: ')
        if response == 'n':
            print('Memorize your passord! GOODBYE!!!')
            break



print("Welcome to Password Picker!!! \n")
choice = input("Would you like to:\n A)customize your password \n B)Use the default password? \n Answer: ")
if choice.upper() == "A":
    custom_pwd()
elif choice.upper() == "B":
    default_pwd()
