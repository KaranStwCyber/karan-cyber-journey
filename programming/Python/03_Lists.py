# ------------------------------
# Lists - Basics
# ------------------------------

friends = ["apple", "34.67", "Orange", "Aero"]
print("Original list:", friends)

# Lists are mutable (can be modified)
friends[0] = "Grapes"
print("After modifying index 0:", friends)

print("Sliced list [1:4]:", friends[1:4])


# ------------------------------
# List Methods
# ------------------------------

friends = ["apple", "34.67", "Orange", "Aero"]

# append() -> adds element at the end
friends.append("Satyawali")
print("After append:", friends)


# ------------------------------
# Numeric List Operations
# ------------------------------

L1 = [1, 8, 7, 2, 21, 15]
print("Original L1:", L1)

# sort() -> sorts in ascending order
L1.sort()
print("After sort():", L1)

# reverse() -> reverses the list
L1.reverse()
print("After reverse():", L1)

# insert(index, value)
L1.insert(3, 8)
print("After insert at index 3:", L1)

# pop(index) -> removes and returns element at index
removed_value = L1.pop(2)
print("After pop(2):", L1)
print("Removed value:", removed_value)

# remove(value) -> removes first occurrence of value
L1.remove(21)
print("After remove(21):", L1)
