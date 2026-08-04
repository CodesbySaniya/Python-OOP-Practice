#methods 

class Employee:

  def __init__(self,name,position):
    self.name = name
    self.position = position

  def get_info(self):
    return f" {self.name} = {self.position}"  #objects in class is known as Instance method

  @staticmethod
  def is_valid_position(position):   #static method does not belong to class objects
    valid_position = ["manager","cook","cashier"]
    return position in valid_position


print(Employee.is_valid_position("cook"))

employee = Employee("saniya","manager")
print(employee.get_info)

