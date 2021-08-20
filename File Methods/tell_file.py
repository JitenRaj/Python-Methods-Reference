# Find the current file position:

f = open("demofile.txt", "r")
print(f.tell())

# Return the current file position after reading the first line:

f = open("demofile.txt", "r")
print(f.readline())
print(f.tell())
