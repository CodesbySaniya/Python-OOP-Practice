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


s1 = Rabbit("bunny",True)
s1.show()
s1.show1()


#multilevel inheritance
#C(B) -> B(A) -> A
# Employee → name, salary, work()
# Manager → manage_team()
# ProjectManager → assign_project()


class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def work(self):
    print("--Employee Details--")
    print(f"Employee name: {self.name}")
    print(f"Employee salary: {self.salary}")

class Manager(Employee):
  def manage_team(self):
    print(f"{self.name} manage the team")

class ProjectManager(Manager):
  def assign_project(self):
    print(f"{self.name} will assign the project")

p1 = ProjectManager("Saniya", 80000)
p1.work()
p1.manage_team()
p1.assign_project()
  
