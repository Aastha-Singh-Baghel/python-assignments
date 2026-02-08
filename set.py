#Create and Access Set Elements
print("create and access set elements")
set_a={10,20,30,40,50}
print("Created Set A:",set_a)

#accessing elements(Itering through the set)
print("Accessing Set Elements:")
for element in set_a:
    print(element,end="")
    print()

#Union of the elements
print("Unioon of the elements")
set_b={40,50,60,70,80}
print("Set B:",set_b)
union_set=set_a.union(set_b)
print("Union of Set A and Set B:",union_set)

#Intersection of the elements 
print("\n Intersectionof the elements")
intersection_set=set_a.intersection(set_b)
print("Intersection of Set A and Set B:",intersection_set)

#Difference of the elements
print("\n Difference of the Elements")
difference_set_a_b=set_a.difference(set_b)#elements in A but not in B
print("Difference of Set A-Set B:",difference_set_a_b)

difference_set_b_a=set_b.difference(set_a)#Elements in B but not in A
print ("Difference of Set B-Set A:",difference_set_b_a)
