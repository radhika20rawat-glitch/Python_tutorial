# When a function calls itself repeatedly called recursion
# Recursive function
def show(n):
    if(n == 0): # <-- base care
      return
    print(n)
    show(n-1)

show(5)