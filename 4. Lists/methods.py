list = [3,8,6,4,9,7]

list.append(10) # adds one element at the end
print("after append ",list)
list.sort() # sorts in ascending order
print("after sort",list)
list.sort(reverse = True) # sorts in descending order
print("after reverse_sort",list)
list.reverse() # reverse list
print("after reverse",list)
list.insert(6,12) # insert element at index
print("after insert",list)

fruits =["Banana","Apple","Mango","Orange"]
print(fruits.append("Grapes"))
print(fruits)