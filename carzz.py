import random

class Car:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Race:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def race(self):
        print("The race starts now!")
        winner = random.choice(self.cars)
        print(f"And the winner is... {winner.name}!")

race = Race()
race.add_car(Car("Red Car"))
race.add_car(Car("Blue Car"))
race.add_car(Car("Green Car"))

race.race()