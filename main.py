from panda import Panda  

panda1 = Panda("Male", 10, 40.5, "Black")
panda2 = Panda("Male", 15, 50.7, "Black and White")
panda3 = Panda("Female", 20, 100, "White")
panda4 = Panda("Female", 30, 110, "Black and White")

# Object One
print(panda1.age)
print(panda1.getColor())
print(panda1.getWeight())
# Object Two
print(panda2.gender)
print(panda2.getColor())
print(panda2.getWeight())
# Object Three
print(panda3.color)
print(panda3.getColor())
print(panda3.getWeight())
# Object Four
print(panda4.weight)
print(panda4.getColor())
print(panda4.getWeight())
