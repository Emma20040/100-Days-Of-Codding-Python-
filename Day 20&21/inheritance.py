class Animal():
    def __init__(self):
        self.number_of_eyes =2

    def breathe(self):
        print("inhale, exhale" )

# inheriting from the animal class
class Fish(Animal):
    def __init__(self):
        super().__init__()

# editin a the method breath from the super class (Animal)
    def breathe(self):
        super().breathe()  
        print("we do this in water") 
    
    def swinm(self):
        print("moving in water")

shark= Fish()
shark.swinm()
shark.breathe()