# Open the file with "a" for appending, then add some text to the file:

f = open("demofile2.txt", "a")
f.write("See you soon!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


# The same example as above, but inserting a line break before the inserted text:

f = open("demofile2.txt", "a")
f.write("\nSee you soon!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
