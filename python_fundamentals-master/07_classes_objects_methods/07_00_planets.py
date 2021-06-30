'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self, name, size, colour):
        self.name = name
        self.size = size
        self.colour = colour

Jupiter = Planet("jupiter", "big", "Green")
print(Jupiter.name)
print(Jupiter.size)
print(Jupiter.colour)


class MyCustomException(Exception):
    def __init__(self, value):
        self.value = value

try:
    raise (MyCustomException(10))
except MyCustomException as error:
    print('A New Exception occurred:', error.value)