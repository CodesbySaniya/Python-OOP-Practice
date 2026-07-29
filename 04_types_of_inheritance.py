#Inheritance types

#1.multiple inheritance = inherit from more then one parent class  C(A,B)

class Prey:
  def __init__(self,name,is_prey):
    self.name = name
    self.is_prey = is_prey

  def show(self):
    print(f"name - {self.name} ")
    print(f"prey- {self.is_prey}")

  
class Predator:
  def __init(self,):
    Predator.is_prey = True

  def show1(self):
    print(f"predators prey")


 
class Rabbit(Prey,Predator):
 print("animals")

# class Hawk:
#   pass

# class Fish:
#   pass

s1 = Rabbit("bunny",True)
s1.show()
s1.show1()
