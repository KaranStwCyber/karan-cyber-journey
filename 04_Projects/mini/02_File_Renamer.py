import os

ol_file = input("Enter The Old File Name: ")
new_file = input("Enter New File Name: ")

os.rename(old_file, new_file)

print("✅ File Renamed Successfully")
