
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food,):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("sage", "dog" , "sit, down, rollover" , 100 , 100)
    def walk(self):
        print(f"{self.first_name}{self.last_name} walks {self.pet.name}. ")
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name}{self.last_name} feeds {self.pet.name}. ")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.first_name}{self.last_name} gives {self.pet.name}  a bath.")
        self.pet.noise()
        return self



class Pet():
    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25
        print(f"{self.name} is going to sleep. zzz")
        print(f"Energy increased by 25, Energy is now: {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Energy increased by 5, Energy is now: {self.energy}\n Health increased by 10, Health is now: {self.health}")
        return self

    def play(self):
        self.health += 5
        print(f"Health increased by 5, Health is now: {self.health}")
        return self

    def noise(self):
        print("Bark!!")
        return self


pet1 = Pet( "sage", "dog", "sit, down, rollover")
ninja1 =Ninja("Mykael", "Sicard", "doggy bacon", "steak")

ninja1.feed()
ninja1.walk()
ninja1.bathe()

print(pet1.tricks)
