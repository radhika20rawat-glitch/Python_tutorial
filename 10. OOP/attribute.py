class Student:
  college_name = "ABC College"
  name = "anonymous" # class attr

  def __init__(self,name,marks):
    self.name = name  # obj attr > class attr
    self.marks = marks
    print("adding new student in database..")

s1 = Student("Radhika",98)
print(s1.name, s1.marks)