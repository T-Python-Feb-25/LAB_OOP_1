# main.py

from panda_class import Panda  # Import the Panda class from the other file

# creating instances/ objects
red_pandas = Panda("Red Pandas", "the eastern Himalayas & southwestern China", "bamboo, fruits, and small animals", 10, "Monday, Thursday")
qinling_pandas = Panda("Qinling Pandas", "the Qinling mountains, China", "bamboo, some fruits", 15, "Friday, Saturday")
sichuan_pandas = Panda("Sichuan Pandas", "the Sichuan province of China", "bamboo, occasionally small animals", 18, "Wednesday, Friday")
giant_pandas = Panda("Giant Pandas", "the mountainous regions of central China", "bamboo, and sometimes small animals", 20, "Tuesday, Thursday")

# print one attribute value for each panda
print(red_pandas.name)  # Printing the name of red pandas

# calling methods on each instance
print(red_pandas.introduce())
print(red_pandas.book_visit())

print(giant_pandas.introduce())
print(giant_pandas.book_visit())

print(sichuan_pandas.introduce())
print(sichuan_pandas.book_visit())

print(qinling_pandas.introduce())
print(qinling_pandas.book_visit())
