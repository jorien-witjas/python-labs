'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

number = int(input("please enter a number between 0 and 10000000: "))

n = 0

while n < 10000:
    if n != number:
        n += 1
    elif n == number:
        break
print(f"the number is found: ",n)