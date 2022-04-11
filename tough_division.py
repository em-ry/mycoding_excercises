#Problem
#Write a function that performs division and prints out the quotient and the remainder.  
# The function should take the numerator and denominator as arguments and not return anything.  
# Note that the function should not simply perform division and display the result as a decimal.  
# Below is a sample execution of the function.
#       >>> divide( 7, 3 )
#		Quotient=[2] Remainder=[1]
#		>>>

#    Modify the above function to return the quotient and the remainder instead of printing them out.  
#    Below is a sample execution of the modified function.
    
#		>>> (quotient, remainder) = divide( 7, 3 )
#       >>> print( quotient, remainder )
#		    2 1


#Precondition
# ?

#Postcondition
#give answer to division as quotient and remainder

#ALGORITHM
#capture numerator and denominator
#use floor division to get quotient
#and use mod to get remainder
#according to my understanding of the question, there will be two functions;
    #one to request for numerator and denominator
    #and the other to perform the operation and return the answer
# my above assumption of the problem was wrong. 
# it says the function should 'print' and not 'return' any value, and both can be handled with the print() function.
# therefore by merging my two functions, the problem is solved.


def capture():
    numerator = float(input('Your numerator is: '))
    denominator = float(input('Your denominator is: '))
    quotient = numerator // denominator
    remainder = numerator % denominator
    print( quotient, remainder)

capture()
# UNRESOLVED PROBLEM
# 1) taking input as float make my results uncontrollable
# 2) taking input as int limits my code to only integers as putting anything else results in an error