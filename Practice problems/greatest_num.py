# WAP to find the greatest of three numbers entered by the user
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
c = int(input("Enter number 3:"))
if( a >= b and b >= c):
  print("First number is greatest : ", a)
elif(b >= c):
  print("Second number is greatest :", b)
else:
  print("Third number is greatest : ",c)