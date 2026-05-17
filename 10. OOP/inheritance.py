'''Inheritance : When one class(child/derived) derives the properties and
   methods of another class(parent/base)
   Types -->
   1. Single Inheritance
   2. Multi-level Inheritance
   3. Multiple Inheritance '''

class Car:
  def __init__(self, typ):
     self.type = type
  
  @staticmethod
  def start():
    print("car started..")

  @staticmethod
  def stop():
    print("car stopped..")

class ToyotaCar(Car):
  def __init__(self,name,type):
    super().__init__(type)
    self.name = name
    super().start()  # Super() method is used to access methods of the parent class
    

car1 = ToyotaCar("prius","electric")
print(car1.type)


class A:
  varA = "Welcome to class A"

class B:
  varB = "Welcome to class B"

class C(A,B):
  varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
