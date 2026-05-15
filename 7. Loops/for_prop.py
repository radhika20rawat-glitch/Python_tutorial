# Print the elements of the following list using a loop

list = [1,2,3,4,5,6,7,8,9]

for i in list:
  print(i)

# Search for a number x in this tuple using loop

tuple = (1,2,3,4,5,6,7,8,9,10)

x = 8
for j in tuple:
  if(j == x):
    print("Found successfully",x)
  else:
    print("Not found")