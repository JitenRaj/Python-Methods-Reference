# User Defined Functions
# Functions Arguments

def print_with_exclamation(word): #this will take a word as arguments
    print(word + "!") # it will add exclamation mark after word

print_with_exclamation("This")
print_with_exclamation("is")
print_with_exclamation("an")
print_with_exclamation("example")
print("\n")

def add_two_strings(word1,word2): # this takes two word as arguments
    print(word1 + " " + word2) # it will add two word with a space

add_two_strings("hello","world")
add_two_strings("Hi","there")
print("\n")

def multiple_strings(word3,x): #this takes two arguments
    multiple = word3*x # it will multiply the strings
    # Condition : we should pass one parameter (or x) => an integer to avoid any error
    print(multiple)

multiple_strings("Hello",3)
multiple_strings("Hey\n",4)