#2. duck tuping method it means that it should have min attributes/method

#if it looks like a duck and quack like a duck,it must be duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

animals = [Dog(),Cat()]

for animal in animals:
    animal.speak()
