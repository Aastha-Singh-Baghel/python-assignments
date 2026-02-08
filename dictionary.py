#Create and Access Dictionary Elements
print("create and access dictionary elements")
my_dict={"name":"Alice","age":25,"city":"New York"}
print("created dictionar:",my_dict)

#Accessing elements
print("Access 'name':",my_dict["name"])#Accessing a value by its key
print("Access'age':",my_dict.get("age"))#Using get() to access a value

#Update Dictionary
print("\n Update Dictionary")
my_dict["age"]=26#Updating an existing key-value pair
print("updated 'age' to 26:",my_dict)

my_dict["profession"]="Engineer"#adding a new key-value pair
print("Added 'profession':",my_dict)

#Removing Elements
print("\n Removing Elements")
removed_value=my_dict.pop("city")#Removing a specific key
print(f"Remove'city':{removed_value}")
print("Dictionary After removing 'city':",my_dict)

del my_dict["name"]#deleting a key value pair
print("Dictionary After Deleting 'name':",my_dict)

my_dict.clear()#clearing all elements from the dictionary 
print("Dictionary After clearinng all elements:",my_dict)

#Merging Dictionaries
print("\n Merging Dictionaries")
dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5}
print("Dictionary 1:",dict1)
print("Dictionary 2:",dict2)

merged_dict=dict1.copy()#copy dict1 into a new dictionary
merged_dict.update(dict2)#merge dict2 into the new dictionary
print("Merged Dictionary:",merged_dict)

