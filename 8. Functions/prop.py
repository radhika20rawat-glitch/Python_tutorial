# WAF to print the elements of a list in a single line.(list is the parameter)

list = [1,2,3,4,5,6,7,8,9,10]

def print_el(list):
  for element in list:
    print(element, end=" ")

print_el(list)