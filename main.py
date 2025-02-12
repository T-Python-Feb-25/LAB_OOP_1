from pand import Panda

panda1 = Panda("Sa", 5, 100, " sushi")
panda2 = Panda("Bu", 3, 45, "burgers")
panda3 = Panda("Mo", 5, 88, " mochi")
panda4 = Panda("Noo", 6, 105, " noodles")

print(f"{panda1.name} {panda1.age} years old")
print(f"{panda2.name} {panda2.age} years old")
print(f"{panda3.name} is {panda3.age} years old")
print(f"{panda4.name} is {panda4.age} yeras old")


panda1.eat()
panda1.sleep()

panda2.eat()
panda2.sleep()

panda3.eat()
panda3.sleep()

panda4.eat()
panda4.sleep()
