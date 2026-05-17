import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
pass_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
  password += random.choice(charvalues)

print("Your random password is :",password)