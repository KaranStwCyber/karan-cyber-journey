#strings

name = "Karan"
name1 = 'karan1'
name2 = '''karan2'''

#string slicing

name3 = "karan3"

nameshort = name3[0:5] # start from index 0 all the way till 5 (excluding 5)
print(nameshort)

character1 = name3[1]
print(character1)


# slicing with skip value
b = "abcdefghijklmnopqrstuvwxyz"
b[1:6:2] #bdf

# string functions
#len:- gives lenth of the string
name = "karan"
print(len(name))
print(name.endswith("ran"))
print(name.startswith("kar"))
print(name.capitalize())

name1 = str(123)
print(f'"{name1}"')

#escape sequence characters

a = "karan is a good boy\nbut not a bad \"boy\""
print(a)
