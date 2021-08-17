# "a" - Append - Opens a file for appending, creates the file if it does not exist

f = open("example.txt", "a")

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

f = open("example.txt", "r")

# "w" - Write - Opens a file for writing, creates the file if it does not exist

f = open("example.txt", "w")

# "x" - Create - Creates the specified file, returns an error if the file exists

f = open("example2.txt", "x")