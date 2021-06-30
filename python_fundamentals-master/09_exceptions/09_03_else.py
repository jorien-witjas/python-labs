'''
Write a script that demonstrates a try/except/else.

'''

try:
    with open("next_travel_destinations", "r") as f1:
except FileNotFoundError:
    with open("next_travel_destinations", "w+") as f1:
        f1.write("Enter all the places you would like to go to: ")
else:
    f1.write("I want to go to Iceland")