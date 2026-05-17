'''Private Attributes & methods
  Conceptual implementation in Python
Private attributes & methods are meant to be used only within the class
and are not accessible from the outside the class'''

class Account:
  def __init__(self,acc_no,acc_pass):
    self.acc_no = acc_no
    self.__acc_pass = acc_pass  #by using 2 underscore we make it private

  def reset_pass(self):
    print(self.__acc_pass)


acc1 = Account("12345","abcde")

print(acc1.acc_no)
print(acc1.reset_pass())