class Class1:
    def __init__(self, x):
        self.x = x
    def get_hello(self, word):
        print(f"Hello {word}")

class Class2(Class1):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def super_prac(self, ball):
        super().get_hello(ball)

b = Class2(10,50)
print(b.y + b.x)
b.super_prac('dog')

# class MyFriend:
#    def sample(self):
#           print("the argument is", self)
# a = MyFriend()
# a.sample()
#
# class MyFriend:
#     def sample(self, argarg):
#         print("the argument is", self)
# a = MyFriend()
# a.sample('hi','hi')

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(5, "world")

square_1 = Square(30)
print(square_1.area())
print(square_1.length)
print(square_1.width)