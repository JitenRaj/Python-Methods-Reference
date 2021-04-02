# String Function

# Join function is used to join all strings in a list
String1=["Benzene","is","a","good","player"]
print(String1) 
print(" ".join(String1))
print(",".join(String1))

# Split functions is used to split a sentence into multiple strings
print("Clash, of, clans, is, a, good, game".split(", "))

# Startswith Function is used to check if a list starts with given word/string
# It returns true or false
print("Benzene is a good player".startswith("Benzene")) # True

print("Benzene is a good player".startswith("good")) # False

# Endswith Function is used to check if a list ends with given word/string
# It returns true or false
print("Benzene is a good player".endswith("player")) # True

print("Benzene is a good player".endswith("is")) # False