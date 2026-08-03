#polymorphism = poly means many and morph means forms  
#ways to acheive 
# 1.inheritance = object treated same as parent class
# 2.duck typing = object must have necessary attributes/methods

from abc import ABC,abstractmethod


class Shape:
  @abstractmethod
  def area(self):
     pass


class Circle(Shape):
   def __init__(self,radius):
      self.radius = radius

   def area(self):
       return 3.14 * self.radius**2
       

class Square(Shape):
   def __init__(self,side):
         self.side = side
   def area(self):
          return self.side * self.side
class Triangle(Shape):
   def __init__(self,base,height):
         self.base = base
         self.height = height
   def area(self):
           return 0.5*self.base*self.height

class Pizza(Circle):
    def __init__(self, radius,topping):
        super().__init__(radius) #using super we inherit method of circle
        self.topping = topping   
   
shapes = [Circle(4),Square(5),Triangle(6,7),Pizza(15,"pepperoni")] #these objects have form of shapes so we can access all shapes together

for shape in shapes:
    print(shape.area())
