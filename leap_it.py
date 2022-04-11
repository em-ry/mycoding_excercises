# write a program to check if a year given is a leap year

#precondition
#a year must be given

#postcondition
# tell if its a leap year or not

#Algorithm
#divide whatever year that is given by 4(if it is greater than 2000)
#or by 400 if it is <= 2000
#then use mod to determine which is or is not a leap year
#display the results


def checker(year:int)->str:
    if year > 2000:
        y1 = year % 4
        if y1 != 0:
            print ('Not a leap year')
        else:
            print ('This is a leap year')
    elif year <= 2000:
        y2 = year % 400
        if y2 != 0:
            print ('Not a leap year')
        else:
            print ('This is a leap year')


print('WELCOME TO LEAP IT!!!!!!!')
print('Be sure to check as many years as you want.')
value = int(input('What year do you want to check: '))
checker(value)