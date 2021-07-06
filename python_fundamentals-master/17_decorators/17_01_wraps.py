"""
Write a decorator function that wraps text passed to it in a html <p> tag.
"""
# def say_hi():
#     print("Hi.")
#
# def say_moo():
#     print("Moooo")
#
# list_ = [say_hi(), say_moo()]   #you store it in a list, but call it at the same time
#
# def outer_func():
#     msg = "Weeeeeekend!"
#     def inner_func():
#         print(msg)
#     return inner_func
# outer_func()


def make_text():
    def wrapper():
        print("Today it is 06 July."
              "The day that I learn to make a decorator."
              "That is awesome")

    return wrapper


