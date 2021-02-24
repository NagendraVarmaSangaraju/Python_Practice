
# #Removing Duplicate words
# st = 'Something is in here Something'
# news = st.split()
# print (" ".join(sorted(set(news),key=news.index)))


# #output
# x= [1,2,3,4,5]
# y=x
# y[2]= 10
# x[3]= 15
# print(x)
# print(y)


# #file handling
# def fil(path):
#     f = open(path+"/bms.py","r")
#     print(f.read())
# path = 'C:/Users/varma/Downloads/Prac'
# fil(path)


#returning all .py files in specific folder
import os
for f_name in os.listdir('C:/Users/varma/Downloads/Prac'):
    if f_name.endswith('.py'):
        print(f_name)

import glob
print(glob.glob('*.py'))


#ABSTRACTION
#IMPLEMENTATION HIDING
#can be achieved using abstract classes and abstract methods
#‘abc’ is the module to be imported when we define an abstract class in Python programs. 
# ‘abc’ stands for ‘abstract base class’.
#Abstract class cannot be instantiated, we cannot create objects for abstract class
from abc import ABC
class Shape(ABC):
    def calculate_area(self):
        pass
class Rectangle(Shape):
    l = 10
    w = 15
    def calculate_area(self):
        return self.l * self.w
class Circle(Shape):
    r = 5
    def calculate_area(self):
        return 3 * self.r

rec = Rectangle()
cir = Circle()
print(rec.calculate_area())
print(cir.calculate_area())


#ENCAPSULATION
#INFORMATION HIDING
#you can achieve encapsulation by protected (_var) and private (__var) members
#you can restrict access to methods and variables
#this can prevent data from being modified by accident and is known as encapsulation.
class Computer():
    def __init__(self):
        self.__maxprice = 900
    def setMaxPrice(self,price):
        self.__maxprice = price
    def sell(self):
        print("selling price: {}".format(self.__maxprice))
c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()


#POLYMORPHISM
#polymorphism an ability to use common interface for multiple forms.
class Parrot:
    def fly(self):
        print ("Parrots can fly")
    def swim(self):
        print ('Parrots cannot swim')
class Penguines:
    def fly(self):
        print ("Pengiunes cannot fly")
    def swim(self):
        print ('Pengiunes can swim')
#common interface
def flying_test(bird):
    bird.fly()

p = Parrot()
pe = Penguines()

flying_test(p)
flying_test(pe)


#INHERITANCE
class Bird:
    def __init__(self):
        print("Bird id instantiated")
    def whoIsThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguine(Bird):
    def __init__(self):
        super().__init__()
        print("Penguine is instantiated")
    def whoIsThis(self):
        print("Penguine")
    def fly(self):
        print("Fly faster")

p = Penguine()
p.whoIsThis()
p.swim()
p.fly()





    





