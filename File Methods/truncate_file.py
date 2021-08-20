# Open the file with "a" for appending, then truncate the file to 20 bytes:

f = open("demofile2.txt", "a")
f.truncate(20)
f.close()

#open and read the file after the truncate:
f = open("demofile2.txt", "r")
print(f.read())
