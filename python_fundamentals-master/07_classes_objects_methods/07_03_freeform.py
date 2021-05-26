'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''
#class food
class food:
    def __init__(self, color, size, taste, sort):
        self.color = color              #objects (/attributes?)
        self.size = size
        self.taste = taste
        self.sort = sort
    def __str__(self):
        return f"the {self.color} {self.sort} is {self.size}"
class clothes:
    def __init__(self, color, size, type):
        self.color = color
        self.size = size
        self.type = type
    def __str__(self):
        return f"my {self.color} {self.type} is too {self.size}"
class furniture:
    def __init__(self, color, size, type, location):
        self.color = color
        self.size = size
        self.type = type
        self.location = location
    def __str__(self):
        return f"the {self.size} {self.color} {self.type} is in  the {self.location}"


#instances
tomato = food("red", "big", "good", "veggie")
apple = food("green", "small", "tasty", "fruit")
print(tomato)
print(apple)

jeans = clothes("blue","trousers", "medium")
coat = clothes("green", "outerwear", "large")
print(jeans)
print(coat)

sofa = furniture("purple", "huge", "sofa", "livingroom")
chair = furniture("red", "petite", "chair", "diningroom")
print(sofa)
print(coat)

print("hi")