# Lists

friends = ["apple", "34.67", "Orange", "Aero"]
print(friends)

friends[0] = "Grapes" # unlike strings lists are mutable
print(friends[0])
print(friends[1:4])

# methods of lists
# append
friends = ["apple", "34.67", "Orange", "Aero"]
friends.append("Satyawali") # append means add anything at the end of the lists
print(friends)

L1 = [1,8,7,2,21,15]

# #sort
L1.sort() # sort the lists in ascending order and uupdates the list
print(L1)

# reverse
L1.reverse() # updates the list to [15,21,2,7,8,1]
print(L1)

# insert
L1.insert(3,8) # this will add 8 at 3 index
print(L1)

#pop
L1.pop(2) # will delete value at index 2 and returns its vakue
print(L1)

# remove
L1.remove(21) # will remove 21 from the list
print(L1)
