'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable
2) Open crime_and_punishment.txt and overwrite the whole content with an empty string
3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.
    a) Which Exception can you expect to encounter? Why?
    b) How do you catch it to avoid the program from terminating with a Traceback?

BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

with open("books/war_and_peace.txt", "r") as wp: #w+ because the file doesn't exist, so now it will create a new file.
    read_wp = wp.read()

with open("books/crime_and_punishment.txt", "r+") as cp:
    cp.read()
    cp.truncate(0)
    cp.write(" ")

with open("books/war_and_peace.txt", "r+") as f1, open("books/crime_and_punishment copy.txt", "r+") as f2, open("books/pride_and_prejudice.txt", "r+") as f3:
    f1 = f1.readlines()
    f2 = f2.readlines()
    f3 = f3.readlines()
    new_list = []
    for item in zip(f1,f2,f3):
        new_list.append(item)
    print(new_list[0])

    for i in new_list[0]:
        print(i[0])