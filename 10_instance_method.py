#methods 

class Employee:

  def __init__(self,name,position):
    self.name = name
    self.position = position

  def get_info(self):
    return f" {self.name} = {self.position}"  #objects in class is known as Instance method


employee = Employee("saniya","manager")
print(employee.get_info())
