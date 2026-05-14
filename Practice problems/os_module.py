# write a python program to print the contents of a directory using the os module
# search outline for the function which does that.
import os

# Specify the directory path
path = "/"


# List and print directory contents
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)

