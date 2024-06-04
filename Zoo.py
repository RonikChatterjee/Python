#   Question6:  Imagine a scenario where you want to model a zoo using Python classes. Design two classes, Animal and Zoo. The Animal class should have attributes like name, species, and age, and the Zoo class should have a list to store instances of Animal. Implement a method in the Zoo class to display information about all the animals in the zoo. Create objects of both classes and demonstrate their usage.

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("Only instances of Animal can be added to the zoo.")

    def display_animals(self):
        if  not self.animals:
            print("There are no animals in the zoo.")
        else:    
            for animal in self.animals:
                print(f"{animal.name} is a {animal.species} that is {animal.age} years old.")

# Creating instances of Animal
lion = Animal(name="Simba", species="Lion", age=5)
elephant = Animal(name="Dumbo", species="Elephant", age=10)
giraffe = Animal(name="Melman", species="Giraffe", age=7)

# Creating an instance of Zoo
zoo = Zoo()

# Adding animals to the zoo
zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(giraffe)

# Displaying information about all animals in the zoo
zoo.display_animals()