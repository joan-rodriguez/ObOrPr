"""This is a class example to understand the basic concepts."""


class Car:
    """This is the car class."""

    def __init__(self, key, wheels, seats, combustible, tank_level):
        self.key = key
        self.wheels = wheels
        self.seats = seats
        self.combustible = combustible
        self.tank_level = tank_level

    def move(self):


    def flat_tire(self):



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