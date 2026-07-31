#method ovetrriding = if there is a same method in super class(parent class) and sub class it will give the result of child class


class Shape:
   def __init__(self,color,is_filled):
      self.color = color
      self.is_filled = is_filled

   def describe(self):
      print(f"it is {self.color} and { 'filled' if self.is_filled == True else 'not filled'}")



class Circle(Shape):
  def __init__(self,color,is_filled,radius):
    super().__init__(color , is_filled)
    self.radius = radius

  def describe(self):
      print(f"the area of a circle is {3.14*self.radius**2} cm^2")


class Square(Shape):
  def __init__(self,color,is_filled,width):
      super().__init__(color , is_filled) 
      self.width = width
  


class Triangle(Shape):
  def __init__(self,color,is_filled,width,height):
      super().__init__(color , is_filled)
      self.width = width
      self.height = height


circle = Circle("red",True,8)

square = Square("blue",False,8)


print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()
