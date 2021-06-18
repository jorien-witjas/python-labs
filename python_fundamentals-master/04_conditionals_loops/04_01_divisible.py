'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

number = int(input("enter a number between 1 and 1000000000: "))

if number %3 == 0:
    print("your number is divisible by 3")
    print(f"the result is: ", number / 3)
else:
    print("your number is not divisible by 3")

print('hello')