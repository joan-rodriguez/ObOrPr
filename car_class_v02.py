"""Car example - Keep it simple!"""
import random


class Car:
    def __init__(self):

        self.possible_colors = ['red', 'blue', 'yellow', 'black', 'white']
        self.engine = False  # True = On // False = Off
        self.max_tank = 50  # liters
        self.tank = random.randint(0, self.max_tank)  # liters
        self.color = random.choice(self.possible_colors)
        self.consumption = 0.07  # liters/km
        self.distance = 0  # km

    def turn_on(self):
        self.engine = True
        print('\nBRrrrRRRRrrrrr... Engine is ON now!')

    def turn_off(self):
        self.engine = False
        print('\nShhhhhhh... Engine is OFF now!')

    def move(self):
        max_dist = round(self.tank / self.consumption, 2)  # km
        print('Current max dist is: {:.2f}'.format(max_dist))  # {:n.mf} ; n = number of figures, m = number of decimals
        while True:
            dist = input('\nHow many km would you like to travel? --> ')
            if not self.engine:
                print('\nI am not an expert, but I think you should turn the engine on first...')
                break
            if str(dist).isdigit():
                if int(dist) > max_dist:
                    self.distance += float(max_dist)
                    self.tank -= round(max_dist * self.consumption, 2)
                    print('\nYour tank is empty. Your car just moved {}km. Total distance is {}km.'
                          .format(max_dist, self.distance))
                    break
                else:
                    self.distance += float(dist)
                    self.tank -= round(float(dist) * self.consumption, 2)
                    print('\nYour car moved {}km! Total distance is {}km.'.format(dist,
                                                                                  self.distance))
                    break
            else:
                print('You need to input a number of km you want to travel.')

    def refill(self):
        max_liters = round(self.max_tank - self.tank, 2)

        while True:
            liters = input('How many liters do you want to refill? --> ')

            if liters.isdigit():
                liters = int(liters)
                break

            print('Must be a number! (you troll)')

        if self.engine:
            print('Hey! Don\'t fill in your tank while... KABOOOOOM!!')
            exit()

        if liters > max_liters:
            self.tank = self.max_tank
            print('\nYou could only fill {}liters in your tank. Now it is full!'.format(max_liters))

        else:
            self.tank += liters

    def paint(self):
        print('\nYour car\'s color is currently {}.'.format(self.color))

        while True:
            new_color = input('What color would you like to paint your car off? --> ')

            if new_color == self.color:
                print('\nPlease... Don\'t waste my time...')
                break

            elif new_color in self.possible_colors:
                self.color = new_color
                print('\nGreat, Sir! Now you have a {} car!'.format(self.color))
                break

            else:
                print('Oooooooh!! This color just got finished... Next week we\'ll have more'
                      ' in store. Until then...')

    def show_status(self):
        print("""
=============================
   --> YOUR CAR STATUS <--
=============================
Color: {}
Tank level: {}liters
Distance: {}km
=============================""".format(
            self.color, self.tank, self.distance
        )
        )


class Manager:
    def __init__(self):
        car = Car()
        print('\nWow! What a brand new car you have there!!\n')
        self.options = {1: car.show_status, 2: car.turn_on, 3: car.turn_off,
                        4: car.move, 5: car.refill, 6: car.paint}

    @staticmethod
    def display_menu():
        print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|      ----> Menu <----     |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| 1- Check out car status   |
| 2- Turn engine ON         |
| 3- Turn engine OFF        |
| 4- Run                    |
| 5- Refill tank            |
| 6- Paint it               |
|                           |
| 7- Exit                   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

    def run(self):
        while True:
            self.display_menu()

            # See function below
            # option = validate_input(
            #     valid_inputs=self.options,
            #     prompt='What do you want to do with your car? --> '
            # )

            option = input('What do you want to do with your car? --> ')

            valid_option = None

            if option.isdecimal():
                option = int(option)

                if option in self.options:
                    valid_option = True
                    # action = self.options.get(option)
                    # action()

                    # Equivalent
                    self.options[option]()

                    input('\n<enter>\n')

                elif option == 7:
                    print('\nLeaving the car in the road, you walk towards the setting Sun...\n')
                    exit()

            if not valid_option:
                print('I\'m sorry, you need to enter one of the options (number)')


"""
def validate_input(valid_inputs, prompt, prompt_fail=None):
    while True:
        option = input(prompt)
        
        if option.isdigit():
            option = int(option)
            if option in valid_inputs:
                return option
        
        if prompt_fail:
            print(prompt_fail)

"""

if __name__ == '__main__':
    Manager().run()
