# Read the content of the file "demofile.txt":

f = open("demofile.txt", "r")
print(f.read())

""" The read() method returns the specified 
number of bytes from the file. 
Default is -1 which means the whole file."""

# Read the content of the file "demofile.txt":

f = open("demofile.txt", "r")
print(f.read(33))
