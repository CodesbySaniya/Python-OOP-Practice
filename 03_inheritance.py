#Inheritance - allow a class to inherit attibutes and objects from another class

class Animals:
  def __init__(self,name,category):
    self.name = name
    self.category = category

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
      print(f"{self.name} is sleeping")

class Dog(Animals):

  def speak(self):
    print("WOOF!")

class Cat(Animals):
  def speak(self):
    print("SQUEEK!")
   

dog = Dog("Dog","pet")
dog.eat()
dog.speak()

cat = Cat("cat","pet")
cat.sleep()
cat.speak()
