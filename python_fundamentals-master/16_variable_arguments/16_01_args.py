'''
Write a script with a function that demonstrates the use of *args.

'''


def my_name(*args):
    for arg in args:
        print(f"My name is: {arg}")


my_name("Jorien", "Peter", "Jessica")