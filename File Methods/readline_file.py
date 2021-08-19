# Read the first line of the file "demofile.txt":

f = open("demofile.txt", "r")
print(f.readline())

# Call readline() twice to return both the first and the second line:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# Return only the five first bytes from the first line:

f = open("demofile.txt", "r")
print(f.readline(5))


""" The readline() method returns one line from the file.

You can also specified how many bytes from 
the line to return, by using the size parameter. """
