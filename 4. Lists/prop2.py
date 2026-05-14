# WAP to check if a list contains a palindrome  of elements 
list1 = [1,2,1]
list2 = [1,2,3]
list3 = ["N","I","T","I","N"]

copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

copy_list3 = list3.copy()
copy_list3.reverse()

if(copy_list1 == list1):
  print("list1 is Palindrome")
else:
  print("Not palindrome")

if(copy_list2 == list2):
  print("list2 is Palindrome")
else:
  print("list2 is Not palindrome")

if(copy_list3 == list3):
  print("list3 is Palindrome")
else:
  print("List3 is Not palindrome")   
