print('Init mammals.py file')


class Mammals:
    def __init__(self):
        """Constructor for this class."""
        print('Initialising Mammals class')
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def print_members(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)


print('Done with init mammals.py file')
