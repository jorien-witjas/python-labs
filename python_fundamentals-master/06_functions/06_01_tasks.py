'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
number = int(input("please enter a number between 1 and 1000000000: "))
def division(number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    else:
        return False
print(division(number))

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

def division_2(number):
    if number % 4 == 0 and number % 7 == 0:
        return True
    else:
        return False
print(division(number))

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables
print(division(number))
output = division(number)

print(division_2(number))
output_2 = division_2((number))
# print your new variables to display the results
print(output, output_2)