# Check if the file is connected to a terminal device:

f = open("demofile.txt", "r")
print(f.isatty())

""" The isatty() method returns True 
if the file stream is interactive, 
example: connected to a terminal device. """
