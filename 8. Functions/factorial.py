# WAF to find the factorial of n.(n is the parameter)
n = int(input("Enter a number: "))


def factorial(n):
  fact = 1
  for i in range(1, n+1):
    fact *= i
  print(fact)

factorial(n)
  