'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():
    def __init__(self, model, year, speed):
        self.model = model
        self.year = year
        self.speed = speed
    def speed_up(self, speed_up, accelate):
        self.accelarate = 5
        self.speed_up = (self.speed + self.accelarate)
        return f"max_speed is {self.speed_up}"
    def __str__(self):
        return f"The {self.model} is from {self.year} and has a max speed of {self.speed_up}"
    # def brake(self):


car_1 = Car('smart', '1993', 210)
car_2 = Car('volvo', '2010', 260)

print(car_1.speed_up(210, 5))
print(car_1.speed_up(210, 5))
print(car_1)

print(car_2.speed_up(260))
print(car_2)
