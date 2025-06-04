import calculator as calc 
import string_utils as str_fun

fact_result = calc.factorial(11)
square_result = calc.square(11)
cube_result = calc.cube(11)


print(f"Factorial of 11 is {fact_result}")
print(f"Square of 11 is {square_result}")
print(f"Cube of 11 is {cube_result}")

reversal  = str_fun.reverse_string("hello")
print(f"Reversed string is : {reversal}")

palindrome_check = str_fun.palindrome("madam")
print(f"Is 'madam' a palindrome? {palindrome_check}")

## importing specific function from string_utils.py 
from string_utils import concatenation_string
## importing all the functions from string_utils.py
from string_utils import * 
s1 = "hello"
s2 = "world"
concatenated = concatenation_string(s1,s2)
print(f"Concatenated string is : {concatenated}")

import math 

print(math.sqrt(17))
print(math.ceil(4.5))
print(abs(-45.4))
print(math.factorial(5))
print(math.pi)

import datetime
today = datetime.date.today()
print(f"Today's data is :{today}")

now = datetime.datetime.now()
print(f"Today's timestamp is : {now}")

import random 
print(random.randint(1, 10))

print(random.uniform(1, 10))

print(random.choice(['apple', 'banana', 'cherry']))
#print(random.rnadn(5, 5))

