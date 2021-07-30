# Get the value of the "age" property of the "Person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')

print(x)

# Use the "default" parameter to write a message when the attribute does not exist:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'page', 'my message')

print(x)