# Change the current file position to 4, and return the rest of the line:

f = open("demofile.txt", "r")
f.seek(4)
print(f.readline())


# Return the new position:

f = open("demofile.txt", "r")
print(f.seek(4))
