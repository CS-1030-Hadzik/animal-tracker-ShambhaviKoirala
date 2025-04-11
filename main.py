#Starting Point
from animal import Animal
from dog import Dog
if __name__ == "__main__":

        ##Bird Section
    bird = Animal("Big Bird", "YellowFeather")
    print(bird)
    bird.speak()

        ##Dog Section
    fido = Dog("Fido", "Canine", "Hound")
    print(fido)
    # TODO: Call the method to make the dog-specific sound
    fido.speak()

    print("All Animals:")
    # TODO print out all the animals
    animals = Animal.get_all_animals()
    for animal in animals:
        print(animal)