'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_name(**kwargs):
    for k,v in kwargs.items():
        print(f"{v} ended in {k} place")


my_name(first="Jorien",second="Peter",third="Jessica")