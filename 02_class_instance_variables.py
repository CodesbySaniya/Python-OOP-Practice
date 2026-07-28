#class variable #created inside the class but outside he method

class Student:
  
  year = 2028 #class variable
  num_stu = 0

  def __init__(self,name,age):
    self.name = name #instance variable
    self.age = age
    Student.num_stu +=1 #for class variable we use class name

s1 = Student("saniya",20)
print(s1.name)
print(s1.age)
print(s1.year) 
print(Student.year)  #give same output as print(s1.year)

print(Student.num_stu)
