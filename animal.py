class Animal:
    """
    Base class representing a generic animal.
    """

    kingdom = "Animalia"

    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species

        Animal.all_animals.append(self)

    # TODO: Add a method to make a generic sound 
    # Call the method `speak` and make it output a specific message like 
    # "The animal makes a noise.""
    def speak(self):
        print("The animal makes a noise.")

    # Example output
    def __str__(self):
        return (f'Kingdom: {self.kingdom }, Name: {self.name}, Species: {self.species }')
    @classmethod
    def get_all_animals(cls):
        return cls.all_animals