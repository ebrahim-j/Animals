from abc import ABCMeta, abstractmethod
#model a Dog object
 
class Animal:
 
    # The init method is called to create an object
    # default values for the fields if none are provided
     

    __metaclass__ = ABCMeta

    def __init__(self, name="", height=0, weight=0):
 
        self.name = name
        self.height = height
        self.weight = weight

 
    def runs(self):
        print("{} runs".format(self.name))
 
    def eats(self):
        print("{} eats".format(self.name))

#must create subclasses with these methods
    @abstractmethod
    def animal_type(self):
        pass
      
    @abstractmethod
    def sound(self):
        pass


#define a cat class inheritting abilitites from animal class 
class Cat(Animal):

    def animal_type(self):
        print("I'm a cat")

    def sound(self):
        print("meow!")

#define a dog class inheritting abilitites from animal class  
class Dog(Animal):

    def animal_type(self):
        print("I'm a dog")

    def sound(self):
        print("woof!")
 
def main():
 
    #Create new cat object
    sparkles = Cat("Sparkles", 25, 16)
 
    sparkles.sound()
    sparkles.animal_type()
    sparkles.runs()
    #new line
    print()

    # Create a new Dog object
    spot = Dog("Spot", 66, 26)
    

    spot.sound()
    spot.animal_type()
    spot.eats()
 
main()