'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length * self.width
        return print(f"the area of the rectangle is {self.area}")
    def perimeter(self):
        self.perimeter()  = 2  * (self.width + self.length)
        return print(f"the perimeter is the rectangle is {self.perimeter}")

rec_1 = rectangle(5, 2)
print(rec_1.area())
print(rec_1.perimeter())


class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self, length, width):
        self.area = length * width
        return print(f"the area of the circle is {self.area}")
    def circumference(self, r):
        self.circumference() = 2 * 3,1415 * self.radius
        return print(f"the circumference of the circle is {self.circumference()}")