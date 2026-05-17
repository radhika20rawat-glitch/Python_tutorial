''' A class method is bound to the class & receives the clas as an implicit first argument.
    Note --> static method can't access or modify class state & generally for unity'''

class Person():
  name = "anonymous"

  # def changeName(self, name):
  #   self.name = name # self.__class__.name = "Radhika Rawat"

  @classmethod                  #decorator
  def changeName(cls,name):
    cls.name = name

p1 = Person()
p1.changeName("Radhika Rawat")
print(p1.name)
print(Person.name)