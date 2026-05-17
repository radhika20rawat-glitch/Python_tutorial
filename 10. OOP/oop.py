'''To map with real world scenarios,we started using objects in code .
This is called object oriented programming
Class is a blueprint for creating objects'''

'''1. Abstraction : Hiding the implementation details of a class and
      only showing the      essential features to the user.
   2. Encapsulation : Wrapping data and functions into a single unit(object).
   3. Inheritance : When one class(child/derived) derives the properties and
      methods of another class(parent/base)
   4. Polymorphism : When the same operator is allowed to have different  to have different meaning according to the context'''

'''1. Static method
   2. Class method(cls)
   3. Instance method(self)'''

# del keyword is used to delete object properties or object itself

# Abstraction
class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False

  def start(self):
    self.clutch = True
    self.brk = True
    print("Car started..")

c1 = Car()
c1.start()
