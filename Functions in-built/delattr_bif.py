# Delete the "age" property from the "person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

print(Person.age)

delattr(Person, 'age')

# error : because age is deleted
print(Person.age)