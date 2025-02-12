'''
Create 4 instances/objects of the class Panda , print 1 attribute value, and call the two methods on each instance.
Note:
Arrange your code in seperate files (one for the main file for main logic , and another for the definition of the class).
'''
from Panda import Panda


#(name, age, weight, habits)
panda1 = Panda("Ping Pan", 10, 250, "Playing With a stick")
panda2 = Panda("Bao Bao", 3, 120, "Climbing")
panda3 = Panda("Mei Mei", 6, 160, "Sleeping")
panda4 = Panda("Tian Tian", 4, 140, "Running")

# Print one attribute value (name) of each panda
print(panda1.name)
print(panda2.name)
print(panda3.name)
print(panda4.name)

# Call the methods on each instance
print(panda1.weights())
print(panda1.add_habits())

print(panda2.weights())
print(panda2.add_habits())

print(panda3.weights())
print(panda3.add_habits())

print(panda4.weights())
print(panda4.add_habits())

'''
this is the first Python lab in the Course
Feb12, 2025
By Mohammed Albushaier
'''
