nums = [1,3,5,2,4]
print("\nDefault lengh :", len(nums))
print(nums)

nums += [7,9,6]
print("length after adding three numbers in list :",len(nums))
print(nums)

nums.append(0)
print("nums list after append(0) :",nums)

nums.insert(2,"python")
print("nums list after inserting python at index[2] :",nums)

print("index of python : ",nums.index("python"))

nums.remove("python")
print("after removing python from list :",nums)

nums.extend([11,15,16,12])
print("after extending the list:",nums)

print("Max number in list is : ",max(nums))
print("Min number in list is : ",min(nums))
