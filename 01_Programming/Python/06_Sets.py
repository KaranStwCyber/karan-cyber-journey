# SETS IN PYTHON

s = {1, 5, 9}
e = set() # don`t use {} to create an empty set as it will create an empty dictionary instead use set() to create an empty set

print(type(e))

# Sets Methods

#add
s = {1,4,65,76,567,44,46,36,97}
s.add(69)
print(s)

#OPERATIONS ON SETS
s = {1,8,2,3}

print(len(s)) # will print the length of set or the number of elements in set
s.remove(8) #updates the set s and removes 8 from s.
print(s)

#union 
s1 = {1,56,9,76,9}
s2 = {5,8,4,5,4}
print(s1.union(s2))

#intersection
s1 = {5,4,36,6,7,5,7,5,6,5,645,9,1,2}
s2 = {4,2,14,5,6}
print(s1.intersection(s2))
