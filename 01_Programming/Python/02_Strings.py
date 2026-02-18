# ------------------------------
# Strings - Basics
# ------------------------------

name = "Karan"
name1 = 'karan1'
name2 = '''karan2'''

print(name)
print(name1)
print(name2)


# ------------------------------
# String Slicing
# ------------------------------

name3 = "karan3"

nameshort = name3[0:5]  # from index 0 to 4
print("Slice 0:5 ->", nameshort)

character1 = name3[1]
print("Character at index 1 ->", character1)


# ------------------------------
# Slicing with Step (Skip Value)
# ------------------------------

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = alphabet[1:6:2]
print("Slice 1:6:2 ->", result)


# ------------------------------
# String Functions
# ------------------------------

name = "karan"

print("Length:", len(name))
print("Ends with 'ran':", name.endswith("ran"))
print("Starts with 'kar':", name.startswith("kar"))
print("Capitalized:", name.capitalize())


# ------------------------------
# Type Conversion to String
# ------------------------------

number = 123
number_str = str(number)
print("Converted to string:", number_str)
print("Type:", type(number_str))


# ------------------------------
# Escape Sequence Characters
# ------------------------------

text = "karan is a good boy\nbut not a bad \"boy\""
print(text)
