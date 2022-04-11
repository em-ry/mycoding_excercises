# problem
#Write a function that converts temperatures from Fahrenheit to Celsius.  
# The function should take the temperature in Fahrenheit as an argument and return the temperature in Celsius. 
#  The function itself should produce no output to the screen.
#formula = (0°C × 9/5) + 32 = 32°F


def converter(temp:float)->float:
    f1 = temp - 32
    f2 = 5/9
    celsius = f1 * f2
    return celsius

    
