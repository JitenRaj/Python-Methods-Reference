# Calculate the length of each word in the tuple:

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)
print(type(x))

#convert the map into a list, for readability:
print(list(x))
