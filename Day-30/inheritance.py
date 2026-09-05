#Inheritance is an OOP concept where one class (child class) gets the properties and 
#methods of another class (parent class). 
#It is mainly used for code reusability.

'''class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)


student = Student("Vikas", 22, 101)

student.display()'''



'''class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


d = Dog()

d.eat()
d.bark()'''

#multiple inheritance
'''class Grandfather:
    def house(self):
        print("House")


class Father(Grandfather):
    def car(self):
        print("Car")


class Son(Father):
    def bike(self):
        print("Bike")


s = Son()

s.house()
s.car()
s.bike()'''

#multilevel inheritance
'''class Grandfather:
    def house(self):
        print("House")


class Father(Grandfather):
    def car(self):
        print("Car")


class Son(Father):
    def bike(self):
        print("Bike")


s = Son()

s.house()
s.car()
s.bike()'''


#Hierarchical Inheritance

'''class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()
'''

#Hybrid Inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


class Pet(Dog, Cat):
    pass


p = Pet()

p.eat()
p.bark()
p.meow()