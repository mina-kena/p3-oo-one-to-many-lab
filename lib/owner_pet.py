class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        if pet_type  not in Pet.PET_TYPES:
            raise TypeError("pet_type must be in PET_TYPES")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
      

class Owner:
    def __init__ (self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        
        if not isinstance(pet, Pet):
            raise TypeError("pet must be of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


p1 = Pet("Rex", "dog")
p2 = Pet("Clark", "cat")

p3 = Pet("Becky", "reptile")
p4 = Pet("Regina", "rodent")
p5 = Pet("sly", "bird")
p6 = Pet("Turuu", "exotic")


# print(Pet.all)

owner1 = Owner("Titus")
owner2 = Owner("Alice")
owner3 = Owner("Kish")

p1.owner =owner1
p2.owner =owner1
p3.owner =owner1

p4.owner =owner2
p5.owner =owner2
p6.owner =owner2

p7 = Pet("Leslie", "dog")


# owner1 = Owner("Titus")
# print("These are Titus' pets....................................................")
# print(owner1.pets())


# print("These are Alice' pets....................................................")
# print(owner2.pets())

owner3.add_pet(p7)
# print("These are owner3 pets....................................................")
# print(owner3.pets())


