"""This is a class example to understand the basic concepts."""
import random


class Car:
    """This is the car class."""

    def __init__(self):
        self.name = 'C4R-'+str(1)
        self.key = None
        self.wheels = self.check_wheels()
        self.seats = 5
        self.tank_level = random.randrange(0, 100)

        self.introduction()

    @staticmethod
    def check_wheels():
        wheels = input('\nSir, how many wheels would you like your car to have? Ask and \n'
                       'you will be provided! --> ')

        error_text = '\nSir, we can be here aaaaall day... But I have cars \n' \
                     'to sell and you might have other people to piss off...\n' \
                     'Now, how many wheels do you want your car to have? --> '

        while True:
            try:
                if int(wheels) > 4:
                    wheels = input('\nSir, you may want to ask for a Truck instead of a \n'
                                   'car... Now, how many wheels do you want your CAR \n'
                                   'to have? --> ')
                elif int(wheels) == 1:
                    wheels = input('\nSir, you may want to ask for a monocycle... Now, how \n'
                                   'many wheels do you want your CAR to have? --> ')
                elif 4 > int(wheels) > 1:
                    wheels = input('\nSir, you may want to ask for a Motorbike instead of \n'
                                   'a car... Now, how many wheels do you want your \n'
                                   'CAR to have? --> ')
                elif int(wheels) == 4:
                    print('\nGreat, Sir! Your 4 wheels are ready to spin!')
                    break

                else:
                    wheels = input(error_text)

            except ValueError:
                wheels = input(error_text)

        return int(wheels)

    def introduction(self):
        print('\nSir, I am pleased to introduce you to your car: {0}.\n'
              'You may like to know that your car has {1} wheels, \n'
              '{2} seats and your tank comes with a {3}% level already filled, \n'
              'Sir. It is on the house :)\n\nNow go and feel the joy of driving!'
              .format(self.name, self.wheels, self.seats, self.tank_level))

    @staticmethod
    def movement():
        print('Move forward. Always.')

    @staticmethod
    def flat_tire():
        print('Your tire is flat man.')


class Key:
    """This is the key class. You will need it to turn your car on."""

    def __init__(self):
        self.key = self.build_it()

    def build_it():
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
        self.welcome()

        self.choices = {
            "1": self.start_engine,
            "2": self.ride,
            "3": self.check_tank,
            "4": self.check_wheels,
            "5": self.pickup_passenger,
            "6": self.leave_passenger,
            "7": self.bike
        }

        self.run()

    @staticmethod
    def welcome():
        print('Dear guest! We are pleased to welcome you to the\n'
              '------------> Ultimate Cars Fair!!! <------------')

    @staticmethod
    def display_menu():
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
            choice = input('\nYou are the driver. You rule. Take an option: --> ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('{0} is not a valid choice.'.format(choice))

    def start_engine(self):
        self.car = Car()
        print('\n----> Engine started.')

    @staticmethod
    def ride():
        print('\n----> You are riding. Like a Pro.')

    @staticmethod
    def check_tank():
        print('\n----> There it is! The tank!')

    @staticmethod
    def check_wheels():
        print('\n----> There are still 4 wheels.')

    @staticmethod
    def change_wheel():
        print('\n----> You change wheel 1 for wheel 3.')

    @staticmethod
    def pickup_passenger():
        print('\n----> Wow! It\'s heavy!')

    @staticmethod
    def leave_passenger():
        print('\n----> Left. Or was it right?')

    @staticmethod
    def refill():
        print('\n----> Refilled with sparkling water.')

    @staticmethod
    def bike():
        print('\n----> See blue anus.')


if __name__ == "__main__":
    Manager()