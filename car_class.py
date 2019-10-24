"""This is a class example to understand the basic concepts."""
import random


class Car:
    """This is the car class."""

    def __init__(self):
        self.key = None
        self.wheels = self.check_wheels()
        self.seats = 5
        self.tank_level = random.randrange(0, 100)

    def check_wheels(self,):
        wheels = input('Sir, how many wheels would you like your car to have? Ask and \n'
                       'you will be provided!')

        while True:
            if wheels > str(4):
                wheels = input('Sir, you may want to ask for a Truck instead of a \n'
                               'car... Now, how many wheels do you want your CAR \n'
                               'to have? --> ')
            elif wheels < str(4):
                wheels = input('Sir, you may want to ask for a Motorbike instead of \n'
                                   'a car... Now, how many wheels do you want your \n'
                                   'CAR to have? --> ')
            elif wheels == str(4):
                print('Great, Sir! Your 4 wheels are ready to spin!')
                break

            else:
                wheels = input('Sir, we can be here aaaaall day... But I have cars \n'
                               'to sell and you might have other people to piss off...')

        return int(wheels)

    def move(self):


    def flat_tire(self):


class Key:
    """This is the key class. You will need it to turn your car on."""

    def __init__(self):
        self.key = self.build_it()

    def build_it(self):
        order = input("Go ahead and build your key (...pressing enter) --> ")
        print("-------------------------------------------\n"
              "The metal those dwarfs gave you in the beginning of time is getting \n"
              "importance right now, right in this place.\n"
              "You are the one who knows how to melt it and how to give it form and \n"
              "properties. The clinging sound of your small hammer is heard in the \n"
              "whole parking lot for the most part of an hour.\n"
              "Finally, the KEY is ready to be used! \n"
              "------------------------------------------")

class Manager:
    """This class manages the options."""

    def __init__(self):
        self.car = Car()
        self.choices = {
            "1": self.start_engine,
            "2": self.ride,
            "3": self.check_tank,
            "4": self.check_wheels,
            "5": self.pickup,
            "6": self.leave,
            "7": self.bike
        }

    def display_menu(self):
        print(
            """

Driver options:
----------------------------------------------
1. Start engine.
2. Ride (like a pro).
3. Check tank.
4. Check wheels.
5. Pick-up passenger.
6. Leave passenger.

7. Be healthy. Leave the car. Take the bike.
----------------------------------------------

"""
        )

    def run(self):
        """Display menu and respond choices."""
        while True:
            self.display_menu()
            choice = input("You are the driver. You rule. Take an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))

    def start_engine(self):


    def ride(self):

    def refill(self):

    def pickup_passenger(self):

    def leave_passenger(self):

    def change_wheel(self):


if __name__ == "__main__":
    Manager().run()