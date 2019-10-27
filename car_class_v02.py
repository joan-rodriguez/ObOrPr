"""Car example - Keep it simple!"""
import random


class Car:
    def __init__(self):
        colors = ['red', 'blue', 'yellow', 'black', 'white']

        self.engine = True
        self.tank = random.random(0, 100)
        self.color = random.random(colors)
        self.consumption = 7  # liters/100km
        self.distance = 0  # km

    def turn_on(self):
        self.engine = True
        print('\nBRrrrRRRRrrrrr... Engine is on now!')

    def turn_off(self):
        self.engine = False
        print('\nShhhhhhh... Engine is off now!')

    def move(self):
        max_dist = self.tank / (self.consumption / 100)  # km
        while True:
            dist = input('\nHow many km would you like to travel? --> ')
            if not self.engine:
                print('\nI am not an expert, but I think you should turn the engine on first...')
                break
            if dist.isdigit():
                if dist > max_dist:
                    self.distance += max_dist
                    print('\nYour tank is empty. Your car just moved {}km. Total distance is {}km.'
                          .format(dist, self.distance))
                else:
                    self.distance += dist
                    print('\nYour car just moved {}km! Total distance is {}km.'.format(dist, self.distance))
