
# Strings and Slicing and F strings

'''
Python string is the collection of the characters surrounded by single quotes, double quotes, or triple quotes. 
Like other languages, the indexing of the Python strings starts from 0.
'''

str = "HELLO"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])

# It returns the IndexError because 6th index doesn't exist
# print(str[6])

# Slicing
str1 = "COMPUTER"

print(str1[0:])  # from start to last

print(str1[1:4])  # print OMP

print(str1[:3])  # By deafult start is 0

# Negative Slicing

print(str1[-1])  # last index

# reverse
print(str1[::-1])

print(str1[-3:])

print(str1[-7:-4])

# steps
print(str1[0::2])


# Reassigning strings
'''
Updating the content of the strings is as easy as assigning it to a new string.
The string object doesn't support item assignment i.e., A string can only be replaced with new string since its content cannot be partially replaced.
Strings are immutable in Python.
'''

# allowed
str = "HELLO"
print(str)
str = "hello"
print(str)

# error - not allowed
# str = "HELLO"
# str[0] = "h"
# #print(str)

# Delete String

'''
As we know that strings are immutable. We cannot delete or remove the characters from the string. 
But we can delete the entire string using the del keyword.
'''

del str


'''
Let's suppose we need to write the text as - They said, "Hello what's going on?"
We can use the triple quotes to accomplish this problem but Python provides the escape sequence.

The backslash(/) symbol denotes the escape sequence.
The backslash can be followed by a special character and it interpreted differently.
'''
# using triple quotes
print('''They said,"What's there?"''')

# escaping single quotes
print('They said, "What\'s going on?"')

# escaping double quotes
print("They said, \"What's going on?\"")

# Hi! "Hurray"
print(' Hi!"Hurray" ')

# 'Hello',"How are u"
print("'Hello',\"How are u\"")

# We can ignore the escape sequence from the given string by using the raw string.
# We can do this by writing r or R in front of the string. Consider the following example.

print(r"C:\\Users\\SIMRAN\\Python32")

# examples
print("C:\\Users\\SIMRAN\\Python32\\Lib")
print("This is the \n multiline quotes")
print("This is \x48\x45\x58 representation")


# format method

'''
The format() method is the most flexible and useful method in formatting strings.
The curly braces {} are used as the placeholder in the string and replaced by the format() method argument.
'''
# Using Curly braces
print("{} and {} both are the best friend".format("Devansh", "Abhishek"))

# Positional Argument
print("{1} and {0} best players ".format("Virat", "Rohit"))

# Keyword Argument
print("{a},{b},{c}".format(a="James", b="Peter", c="Ricky"))

# String Function .. there are some in built string functions you can google them..

name = "mapari Simran"
print(name.capitalize())  # It capitalize only 1st letter and keeps rest lower

print(name.upper())  # convert in upper case

num = "10002"
print(num.isnumeric())

# replace

print(name.replace("Simran", "arzoo"))

# split - It returns list

color = "green,orange,red,blue"
print(color.split(','))

print(name.split(' '))


# join
lst = ['simran', 'is', 'a', 'good', 'girl']

new_str = ' '.join(lst)
print(new_str)


# F strings

name = 'Simran'
age = 21
print(f"Hello, My name is {name} and I'm {age} years old.")

print(f"{name} is {age} years old")
