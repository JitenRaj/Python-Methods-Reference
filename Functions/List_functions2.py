# List Functions
# List of words
words = ["Python", "are", "a", "programming" ,"language","!!"] # creating a list with a variable name "words"
print(words) # to print the list

words.insert(1,"is") # to insert "is" at index 1
print(words)

words.remove("are") # to remove "are" from the list
print(words)

print(words.count("!!")) # to count the number of time an item appears

print(words.pop(5)) # to pop/remove an item from a specific index position
print(words)

print(words.reverse()) # to reverse the list
print(words)

print(words.reverse()) # to reverse the list

words.clear() # to remove all items from a list, we use .clear()
print("after clearing the list:",words)

