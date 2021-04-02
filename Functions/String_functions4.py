# String Functions

# Upper functions is used to make all the latters/string Upper case
print("Benzene is a good player".upper())

# Lower functions is used to make all the latters/string Lower case
print("BENZENE IS A GOOD PLAYER".lower())

# Replace function is used to replace one string with another
print("Benzene","is","a","good","player".replace("player","scammer"))

# Find functions is used to find the index postion of given string/letter
print("Benzene is a good player".find("is"))
print("Benzene is a good player".find("good"))

# isalpha functions is used to check if all character are alphabet in a string
print("Benzene is a good player".isalpha()) #False because spaces
print("Benzene".isalpha()) #True

# isnum functions is used to check if all character are numbers
print("benzene123".isnumeric()) # False
print("1234".isnumeric()) # True