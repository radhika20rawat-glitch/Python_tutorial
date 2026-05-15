# WAP to search for a number x in this tuple using loop

tuple = (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0
while i<len(tuple):
    if(tuple[i] == x):
      print("Found at index",i)
    else:
      print("finding")
    i += 1