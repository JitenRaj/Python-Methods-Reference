""" To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:"""

f = open("example.txt","r")

print(f.read())

# Return the 5 first characters of the file:

f = open("example.txt", "r")
print(f.read(5))

# Open a file on a different location:

f = open("D:\GitHub\Python-Practice\README.md", "r")
print(f.read())