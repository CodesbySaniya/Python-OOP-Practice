#oops concept contain attributes(data) and method(function)
#we create an class first then in this class we create object and methods

class Student:
  def name(self):
    sname = "saniya"
    year = "3rd"
    print(f"Hello {sname} , you are in {year} year")

student1 = Student()
student1.name()
  

#using constructor

class Students:
  def __init__(self,name,year,roll_no):
    self.name = name
    self.year = year
    self.roll_no = roll_no

  def show1(self):
     print(f"{self.name} year {self.year} roll_no {self.roll_no} you are pass")

s1= Students("saniya","3rd","041")
s1.show1()


class Car:
  def __init__(self,model,year,color,for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

  def show(self):
    print("DETAILS OF CARS")
    print(f"Model name : {self.model}")
    print(f"Model year: {self.year}")
    print(f"Model colour : {self.color}")
    print(f"Model for_sale : {self.for_sale}")

s2 = Car("BMW",2024,"Red",True)
s2.show()
