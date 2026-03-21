# FILE OPEN

f = open("file.txt")
data = f.read()
print(data)
f.close()

#FILE WRITE

st = "Hey karan you are amazing"
f = open("Myfile.txt", "w")
f.write(st)
f.close

# FILE FUNCTIONS 

#READLINES()
f = open("file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()

#Readline()

f = open("file.txt")
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

f.close()

#append mode:- add the text in the end of the file

str = "HEy BOY!\n" # wiill add the text in new line to avoid confusion in the code
line = open("file.txt", "a")
line.write(str)
line.close()

#with
f = open("file.txt")
print(f.read())
f.close()

# we can use with to write the same code and we don`t have to write close() at the end of the code

with open("file.txt") as f:
    print(f.read())
