# String Functions Demonstration in One Code

text = "  Python Programming is AWESOME  "
print("Original String:", text)

# Length
print("Length:", len(text))

# Replace
print("Replace:", text.replace("AWESOME", "FUN"))

# Find & Count
print("Find 'Programming':", text.find("Programming"))
print("Count 'o':", text.count("o"))

# Startswith & Endswith
print("Starts with '  Py':", text.startswith("  Py"))
print("Ends with 'ME  ':", text.endswith("ME  "))

# Splitting
words = text.split()
print("Split:", words)

# Joining
joined = "-".join(words)
print("Join:", joined)

# Formatting (f-string)
name = "Radhika"
age = 18
print(f"My name is {name} and I am {age} years old")

# Center, Left, Right
sample = "Python"
print("Center:", sample.center(10, "*"))
print("Left Justify:", sample.ljust(10, "-"))
print("Right Justify:", sample.rjust(10, "-"))
