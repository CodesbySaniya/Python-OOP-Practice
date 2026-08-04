class Student:
  count = 0 

  def __init__(self,name,gpa):
    self.name = name
    self.gpa = gpa
    Student.count +=1


  #INSTNCE METHOD
  def get_info(self):
    return f"{self.name} = {self.gpa}"

  #CLASS METHOD
  
  def get_count(cls):
    return f"total number of student = {cls.count}"


student = Student("saniya",9.99)

print(Student.get_count())
