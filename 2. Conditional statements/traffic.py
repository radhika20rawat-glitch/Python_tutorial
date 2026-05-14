# WAP to display traffic light rules
colour=input("Enter colour of light: ")
if(colour == "red"):
  print("Stop")
elif(colour == "green"):
  print("Go")
elif(colour == "yellow"):
  print("Ready")
else:
  print("Light is  Broken")