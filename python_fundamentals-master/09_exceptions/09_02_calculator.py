'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

num_1 = input("please give me a number: ")
num_2 = input("please give me another number: ")
try:
    quotient = int(num_1) / int(num_2)
    print(quotient)
except ValueError:
    print("please enter a number and no letters")
except ZeroDivisionError:
    print("please pick another number than zero")
