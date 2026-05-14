#string declaration
name1="Radhika"
name2='Radhika'
name3='''Radhika'''
print(name1)
print(name2)
print(name3)


#Slicing of strings
nameshort =name1[0:5]
print("nickname:",nameshort) #start from index 0 and print all the way till 5(excluding 5)
print(name1[-6:-1])
print(name1[1:])
print(name1[:6])

#slicing using skipvalue
a="Software Engineer"
print(a[1:15:2])