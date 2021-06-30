'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class rectangle:
    square = True                   #class variable
    def __init__(self, length, width):
        self.length = length        #attributes (variables that are only defined in init)
        self.width = width
        self.area = self.length * self.width
        self.perimeter = 2 * (self.width + self.length)
    def __str__(self):
        return f"the area of the rectangle is {self.area} and the perimeter is the rectangle is {self.perimeter}"

rec_1 = rectangle(5, 2)
print(rec_1)

class circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = (3.1415 * self.radius ** 2)
        self.circumference = 2 * 3.1415 * self.radius
    def __str__(self):
        return f"the area of the circle is {self.area} and the circumference of the circle is {self.circumference}"

circle_1 =  circle(3)
print(circle_1)