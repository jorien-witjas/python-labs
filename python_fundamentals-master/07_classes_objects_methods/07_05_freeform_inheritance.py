'''
Build on your previous freeform exercise.
    Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.
    Build these classes out like we did in the previous exercises.
    If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.
    We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:
    - A Vehicle superclass, with Truck and Motorcycle subclasses.
    - A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

#Amsterdam

class CityActivities:
    def __init__(self, activity, season, time, amount_pp):
        self.activity = activity
        self.season = season
        self.time = time
        self.amount_pp = amount_pp

class Restaurants(CityActivities):
    def __init__(self, activity, season, time, amount_pp, sort):
        super().__init__(sort)
        self.sort = sort

class Pubs(Restaurants):
    pass

Volt = Pubs("eating", "all", "evening", "4_max", "pub")

print(volt.activity)