#PROBLEM
# Write a function that computes the total amount of money you would receive if you received a penny a day doubled a day for a month. 
# For example, on the first day you would get $0.01, on the second day you would get $0.02 (for a total of $0.03), 
# on the third day you would get $0.04 (for a total of $0.07), and so on.  
# Your function should take the number of days in the month as an argument and return the total amount of money you would receive.  
# Furthermore, the function should print out the amount received for each day and the current total up to that day.

#precondition
# the arguments must be positive integers

#postconditions
# 2 results to be displayed
    # daily income and total income

#ALGORITHM
# using the fibonancci series formula
    #add 1 to every nth sum




days = int(input('How many did you work: '))

def checker(input:int)->float:
    #n1 ,n2 is day1 and day2
    n1,n2 = 1, 2
    count = 0
    if input == 0:
        print('Sorry, no salary for you.')
    elif input == 1:
        print(n1)
    else:
        # my precondition, though not sure if it is necessary
        while input > 0:
            while count < input:
                nth = n1 + n2 + 1
                print('Your daily salary is: $',n1 / 100)
                n1 = n2
                n2 = nth
                count += 1
                # float goes haywire after third iteration
                # stackoverflow says its because of the exponent and mantissa method used by float() funtions
                #solution: i worked with the salary as whole numbers and just before results are projected,
                # i divide them by 100 to get a 2 decimal place answer.
                new = nth / 100 
            return  'Your total salary is: $',new
            
        #break : interpreter is telling me--> "break" can be used only within a loop
        input = 0
        

print(checker(days))
