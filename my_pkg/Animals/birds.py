from Animals.sub_pkg_1 import cool_tools


class Birds:
    def __init__(self):
        """Constructor for this class."""

        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']

    def print_members(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)

    def crazy_bird(self):
        print('Calling coolest() from bird.py')
        cool_tools.coolest()
