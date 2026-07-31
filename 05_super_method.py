#super class -  inherit method of super class to sub class


class Shape:
   def __init__(self,color,is_filled):
      self.color = color
      self.is_filled = is_filled




class Circle(Shape):
  def __init__(self,color,is_filled,radius):
    super().__init__(color , is_filled)
    self.radius = radius


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



print(square.color)
print(square.is_filled)
print(square.width)
