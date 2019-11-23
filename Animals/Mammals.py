class Mammals:
    def __init__(self):
        """Constructor for this class."""

        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def print_members(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
