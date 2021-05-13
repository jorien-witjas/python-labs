'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
#not sure if I understood the exercise correctly

number = int(input("please enter a number: "))

if number > 12:
    print("Equals Other")
else:
    if number == 1:
        print("Equals January")
    elif number == 2:
        print("Equals February")
    elif number == 3:
        print("Equals March")
    elif number == 4:
        print("Equals April")
    elif number == 5:
        print("Equals May")
    elif number == 6:
        print("Equals JUne")
    elif number == 7:
        print("Equals July")
    elif number == 8:
        print("Equals August")
    elif number == 9:
        print("Equals September")
    elif number == 10:
        print("Equals October")
    elif number == 11:
        print("Equals November")
    elif number == 12:
        print("Equals December")
