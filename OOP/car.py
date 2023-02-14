class car():
    def __init__(self,price,owner,model,color):
        self.price=price
        self.owner=owner
        self.model=model
        self.color=color

buyer_one=car("1.8M","vincent","landcruiser TX","Black")
print(buyer_one.price)
print(buyer_one.owner)
print(buyer_one.model)
print(buyer_one.color)


print("-----------End of buyer_one")


buyer_two=car("1.5M","Belinda","Toyota Premio","pearl white")
print(buyer_two.price)
print(buyer_two.owner)
print(buyer_two.model)
print(buyer_two.color)


print("-----------End of buyer_two")


buyer_three=car("1.2M","Victor","Mazda Axela","pure black")
print(buyer_three.price)
print(buyer_three.owner)
print(buyer_three.model)
print(buyer_three.color)


print("-----------end of buyer three")