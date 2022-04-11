#Problem
# Write a function that prompts the user for input, changes the input so that it is in all capital letters and prints it out.
# The function should continue to prompt for input until the user enters `quit`.


def letters(word:str)->str:
    phrase = ''
    while word != 'quit':
        phrase = phrase + word.upper() + ' ' + '\n'
        word = input('Say something: ')
    return phrase

    


# how does one increase a string?
#solved this by manipulating the strings before storing



print(letters(input('Say something: ')))
#Errors in this code:
    # 1) the first input is not accounted for
    # 2) i'm using two variables whereas i want to use only one

#errors corrected!!!
#the first input was not accounted for because it was stored outside the while loop
#the second error was corrected by using the temporal variable in the function as the second variable
# best of all, by using concatination/ string manupulation, i'm able to add some space between each word
# on the plus side, my code has become shorter.(correction tips gotten from giraffe academy tutorial)