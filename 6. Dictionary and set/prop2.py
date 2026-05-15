''' WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
 Start with an empty dictionary and add one by one .
 Use subject name as key and marks as value''' 

result = {}

x = int(input("Enter physic marks: "))
result["Physic"] = x

x = int(input("Enter chemistry marks: "))
result["chemistry"] = x

x = int(input("Enter Maths marks: "))
result["Maths"] = x

print(result)