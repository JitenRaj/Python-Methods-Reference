num = input("Enter a number: ")
def factorial(n):
if n == 1:
   return n
elif n < 1:
   return ("NA")
else:
   return n*factorial(n-1)
print(factorial(int(num)))
