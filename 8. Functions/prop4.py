def print_list(list, idx=0):
    if(idx == len(list)):
       return 
    print(list[idx])
    print_list(list,idx+1)

fruits = ["Mango","Apple","Banana","Orange","Litchi","Watermelon"]

print_list(fruits)