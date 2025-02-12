from panda import Panda

panda1 = Panda("jojo", 5, 100, "Black & White")
panda2 = Panda("Momo", 3, 80, "Brown")
panda3 = Panda("Lulu", 4, 90, "Golden")
panda4 = Panda("Bamboo", 2, 70, "Black & White")

pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(f"Panda Name: {panda.name}")
    print(panda.eat("bamboo"))
    print(panda.sleep())
    print("-" * 30)
