# Loops in Python

print(1)
print(2)
print(3)
print(4)
print(5)

# this task can also be done like this 

for i in range(1,6):
    print(i)
    
#2 while loops

i = 1
while(i<51):
    print(i)
    i+=1
    
'''
Output:
1
2
3
4
5
'''

#3 list while

l = [1,2, 3, "Karan", "Satyawali", "Python"]
i = 0
while(i<len(l)):
    print(l[i])
    i+=1
    
#4 for loops

for i in range(1,100,4):
    print(i)
    
#5 for loops iterate

## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)
    
#6 for with else

i = [1,2,3,4,5,6,7,8,9]
for list in i:
    print(list)
else:
    print("Done")
    
#7 break and contimue

for i in range(100):
    if(i==34):
        break # cut the loop right away
    print(i)
    
for i in range(100):
    if(i==34):
        continue
    print(i)
    
#8 pass
for i in range(1,45):
    pass

i = 0
while(i<45):
    print(i)
    i+=1
