# Clever if / Ternary Operator
# syntax <var> = (false_val, true_val)[<condtion>]

age = int(input("Enter your age: "))
vote = ("Yes you can vote", "No , you can't vote")[age<18]
print(vote)

sal=float(input("Enter your salary:"))
tax = sal*(0.1, 0.2) [sal<=50000]
print(tax)