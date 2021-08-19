# Return all lines in the file, 
# as a list where each line is an item in the list object:

f = open("demofile.txt", "r")
print(f.readlines())


# Do not return the next line if the total number of returned bytes are more than 33:

f = open("demofile.txt", "r")
print(f.readlines(33))
