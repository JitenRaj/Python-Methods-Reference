# List Functions
# List of numbers
numbers = [1,3,5,2,4] # creating a list with a variable name "numbers"

print("\nDefault length of list :", len(numbers)) # to check & print the lenght of the list
print(numbers) # to print the list

numbers += [7,9,6] # to add items/list in the list
print("length after adding three numbers in list :",len(numbers)) 
print(numbers)

numbers.append(0) # to add an item in end of the list, we use list.append()
print("list after append(0) :",numbers)

numbers.insert(2,22) # to add an item at desired position in the list, we use list.insert()
print("list after inserting a num :",numbers)

numbers.extend([11,15,16,12]) # to extend the list by adding items/lists, we use list.extend()
print("after extending the list:",numbers)

numbers.remove(0) # to remove a num from list, we use list.remove()
print("after removing a num from list :",numbers)

print(numbers.sort()) # to short a list in accending order
print(numbers)

print("Max number in list is : ",max(numbers)) # to check maximum num in list
print("Min number in list is : ",min(numbers)) # to check minimum num in list
