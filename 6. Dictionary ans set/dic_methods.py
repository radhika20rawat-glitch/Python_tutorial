dict ={"name":"Radhika","College":"MDU Rohtak","CGPA":"9.6"}
print(dict.keys())
print(dict.values()) #return all values
print(list[dict.values()]) # covert into list
print(len(list(dict.values()))) #return length
print(dict.items()) # returns all keys:values
print(dict.get("name")) #return key acoording to value
print(dict.update({"city":"Palwal"}))
print(dict)