class House():
    def __init__(self,type,location,owner):
        self.type=type
        self.location=location
        self.owner=owner

owner_one=House("Bungalow", "Kitengela","chris")
print(owner_one.type)
print(owner_one.location)
print(owner_one.owner)

print("-----end of owner_one")

owner_two=House("penthouse","Kitusuri","Mutinda")
print(owner_two.type)
print(owner_two.location)
print(owner_two.owner)

print("---------------------end of owner_two")










