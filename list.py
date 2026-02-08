#Create and access list elements
print("create and access list elements")
my_list=[10,20,30,40,50]
print("created list:",my_list)
print("Access Element at Index 2:",my_list[2])

#Add and Remove list Elements 
print("\n Add and REmove List Elements")
my_list.append(60)
print("List After Adding 60:",my_list)

my_list.insert(2,25)
print("List After Inserting 25 at Index 2:",my_list)

my_list.remove(30)
print("List After Removing 30:",my_list)

popped_element =my_list.pop()
print("popped element:",popped_element)
print("List After Popping last element:",my_list)

#Sort list elements 
print("\n Sort list elements")
my_list.sort()
print("List After Sorting in Ascending Order:",my_list)

my_list.sort(reverse=True)
print("List After sorting in Decending Order:",my_list)

#Reverse list elements
print("\n Reverse List Elements")
my_list.reverse()
print("List After Reversing:",my_list)