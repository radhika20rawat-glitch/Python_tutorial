# WAP to find the sum of first n numbers .(using while)

n = int(input("Enter number:"))
sum = 0
i = 0
while i <= n:
  sum += i
  i += 1

print("Total sum is",sum)