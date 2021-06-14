'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

try:
    num_1 = int(input("please give me a number: "))
    num_2 = int(input("please give me another number: "))
except ValueError:
    print("please enter a number and no letters")
else:
    print("good job!")