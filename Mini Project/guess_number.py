import random

target = random.randint(1,100)

while True:
  userChoice = input("Guess the target or Quit(Q) : ")
  if(userChoice == "Q"):
    break

  userChoice = int(userChoice)
  if(userChoice == target):
    print("Success : correct Guess!!")
    break
  elif(userChoice < target):
    print("Your number was small.Take a bigger guess...")
  else:
    print("Your number was large. Take a small guess...")
  
print("------GAME OVER------")