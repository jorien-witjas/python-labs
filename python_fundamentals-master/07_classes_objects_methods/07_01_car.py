'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class car():
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = int(max_speed)

    def speed_up(self, speed):
        print("max_speed is " + (int(speed) + int(self.max_speed))

smart = car("smart", "1993", 210)
print(smart.model)
print(smart.year)
print(smart.speed_up(5))
volvo = car("volvo", "2010", 260)
print(volvo.model)
print(volvo.year)
print(volvo.speed_up(5))
