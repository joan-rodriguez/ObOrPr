print('Start execution')

# Import classes from your brand new package
from Animals.birds import Birds
from Animals.mammals import Mammals
from Animals.sub_pkg_1 import cool_tools

print('Finish imports')

# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.print_members()

print('Calling coolest() from main.py file')
cool_tools.coolest()

# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.print_members()
myBird.crazy_bird()
