'''Constructor :All classes have a function called _init_(), which is always executed when the object is being initiated
def _init_(self,fullname):
The self parameter is a reference to the current instance of the class, and is used to access variables 
that belongs to the class'''

class Student:

  #default constructors
  def __init__(self):
    pass
  
  #parameterized constructors
  college_name = "ABC College"
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks
    print("adding new student in database..")
    
s1 = Student("Radhika",98)
print(s1.name, s1.marks)

s2 = Student("Panchi",87)
print(s2.name, s2.marks)

print(s2.college_name)