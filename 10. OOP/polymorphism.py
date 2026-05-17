''' Polymorphism : Operator Overloading
When the same operator is allowed to have different  to have different meaning according to the context
Operators & Dunder functions
a+b addition             a.__add__(b)
a-b subtraction          a.__sub__(b)
a*b multiplication       a.__mul____(b)
a/b division             a.__truediv____(b)
a % b modulus            a.__mod____(b)   '''       

class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img

  def showNumber(self):
    print(self.real,"i +", self.img,"j")

  def __add__(self,num2):
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal, newImg)
    

  def __sub__(self,num2):
    newReal = self.real - num2.real
    newImg = self.img - num2.img
    return Complex(newReal, newImg)
    


num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(6,8)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()