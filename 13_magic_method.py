#magic methods
#they are dunder method which is automatically called by python

class Book:


  def __init__(self,title,author,num_pages):
    self.title = title
    self.author = author
    self.num_pages = num_pages

  def __str__(self):                          #customize string representation of aan object
    return f"{self.title} by {self.author}"

  def __eq__(self, value):
    return self.title == value.title and self.author == value.author

  def __lt__(self,other):                     #less than function to compare
    return self.num_pages < other.num_pages

  def __gt__(self,other):                     #greater than function to compare
    return self.num_pages > other.num_pages
  
  
book1 = Book("abc"," thomsan",90)
book2= Book("xyz","vex king",109)
book3 = Book("abc"," thomsan",90)
print(book1)
print(book2)
print(book1==book3)     #both are same but not giving output as True so we use __eq__
print(book1 < book2)    #for less than
print(book1>book2)      #for greater than
