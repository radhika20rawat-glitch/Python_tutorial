''' Python features seven primary types of operators that allow you to perform various operations on values, known as operands:

Arithmetic Operators: Used for mathematical calculations:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulus/Remainder)
** (Exponentiation)
// (Floor Division)

Assignment Operators: Used to assign values to variables:
= (Assign)
+= (Add AND Assign)
-= (Subtract AND Assign)
*= (Multiply AND Assign)

Comparison (Relational) Operators: Used to compare values, returning True or False:
== (Equal to)
!= (Not equal to)
< (Less than)
> (Greater than)
<= (Less than or equal to)
>= (Greater than or equal to)

Logical Operators: Used to combine conditional statements:
and
or
not

Identity Operators: Used to compare the memory locations of two objects:
is
is not

Membership Operators: Used to test if a value is present in a sequence (e.g., a list or string):
in
not in

Bitwise Operators: Used to perform operations on individual bits of numbers:
& (AND)
| (OR)
^ (XOR)
~ (NOT)
<< (Left Shift)
>> (Right Shift)
These operators enable various functionalities, including calculations, comparisons, and data manipulation, which contribute to more concise and powerful code '''


# Arithmetic Operators
a=int(input("Enter a :"))
b=int(input("Enter b :"))
num=int(input("Enter num :"))
print(a+b) 
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)


# Assignment Operators
num = num + 4
num /= 4
num -= 6
print("num :", num)


#Relational Operators
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)

# Logical Operators
print( not False)
print( not True)
val1 = True
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)
