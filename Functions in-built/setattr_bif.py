# Change the value of the "age" property of the "person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

print(Person.age)