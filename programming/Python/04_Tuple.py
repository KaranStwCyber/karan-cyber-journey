# ------------------------------
# Tuples in Python
# ------------------------------
# A tuple is an immutable data type (cannot be modified after creation)

a = ("Karan", 1, 3, 7, False)

print("Tuple:", a)
print("Type:", type(a))


# ------------------------------
# Tuple Methods
# ------------------------------

a1 = (1, 2, 3, 8, 98, 5, 8, 98, 4, 7)
print("Original tuple:", a1)

# count(value) -> returns number of occurrences
count_98 = a1.count(98)
print("Count of 98:", count_98)

# index(value) -> returns first index of value
index_2 = a1.index(2)
print("Index of 2:", index_2)
