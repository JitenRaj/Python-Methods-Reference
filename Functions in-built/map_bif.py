# Calculate the length of each word in the tuple:

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)
print(type(x))

#convert the map into a list, for readability:
print(list(x))

# Make new fruits by sending two iterable objects into the function:

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))