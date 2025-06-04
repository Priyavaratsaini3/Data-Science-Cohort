## This file is working as a module where all the required funtion are defined

def square(num):
    """This function returns the square of a number """
    return num ** 2

def cube(num): 
    return num ** 3

def factorial(n):
    ## base case condition
    if n == 0 or n == 1:
        return 1 
    ## recursive call 
    return n * factorial(n - 1)

def add(num1, num2):
    return num1 + num2 

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2 ):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Can not divide by zero"
    else: 
        return num1 / num2

    