#problem
#Write a function that converts distances from miles to kilometers. 
# The function should take the distance in miles as an argument and return the distance in kilometers.  
# The function itself should produce no output to the screen.


def converter(dist:float)->float:
    # 1 mile = 1.60934 kilometers
    return dist * 60934