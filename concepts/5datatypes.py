# Data Types in Python

'''
Variables can hold values, and every value has a data-type. 
Python is a dynamically typed language; hence we do not need to define the type of the variable while declaring it. 
The interpreter implicitly binds the value with its type.

Python provides various standard data types that define the storage method on each of them. 
The data types defined in Python are given below.
1. Numbers - integer , float , complex
2. Sequence Type - string , list , tuple
3. Boolean
4. Set
5. Dictionary
'''

# Numbers
'''
Number stores numeric values. The integer, float, and complex values belong to a Python Numbers data-type. 
Python provides the type() function to know the data-type of the variable.
Similarly, the isinstance() function is used to check an object belongs to a particular class.
'''

a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1+3j
print("The type of c", type(c))
print("c is a complex number", isinstance(1+3j, complex))

# Sequence Type - we will see further this concepts in detail for now just lets see basic of it.

# String
'''
The string can be defined as the sequence of characters represented in the quotation marks. 
In Python, we can use single, double, or triple quotes to define a string.
In the case of string handling, the operator + is used to concatenate two strings as the operation "hello"+" python" returns "hello python".
The operator * is known as a repetition operator as the operation "Python" *2 returns 'Python Python'.
'''

str = "Python is a programming" + " language"
print(str)
print("Simran"*2)

# basic string handling
str1 = "Simran"
str2 = "Mapari"

# indexing starts from 0

print(str1 + str2)  # concatenation of str1 and str2

print(str1[0:3])  # print first 3 letters

print(str2[2])  # print p


# List
'''
Python Lists are similar to arrays in C. However, the list can contain data of different types.
The items stored in the list are separated with a comma (,) and enclosed within square brackets [].
It is mutable - we can modify it.
'''

lst = [1, 2, "simran", 6, 13.5, 'abc']
print(type(lst))

print(lst[1])  # print element on 1st position .. starts from 0

lst[1] = 10  # changing value of 1st position

print(lst)

# we will see it in detail in list.py further...

# Tuple
'''
A tuple is similar to the list in many ways. Like lists, tuples also contain the collection of the items of different data types. 
The items of the tuple are separated with a comma (,) and enclosed in parentheses ().
A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple.
'''
tup = ("hi", "Python", 2)

# Checking type of tup
print(type(tup))

# try to change value      tup[1] = "program" - It will give error
print(tup)

# Tuple slicing
print(tup[1:])
print(tup[0:1])

# Tuple concatenation using + operator
print(tup + tup)

# Tuple repatation using * operator
print(tup * 3)

tup1 = ('Simran')
print(type(tup1))  # it will say string

# If you have 1 element in tuple then declare it like this
tup2 = ('Mapari',)
print(type(tup2))

# Boolean
'''
Boolean type provides two built-in values, True and False. 
These values are used to determine the given statement true or false.
It denotes by the class bool. True can be represented by any non-zero value or 'T' whereas 
false can be represented by the 0 or 'F'.
'''
a = True
print(type(a))
b = False
print(type(b))


# Set
'''
Python Set is the unordered collection of the data type. 
It is iterable, mutable(can modify after creation), and has unique elements.
The set is created by using a built-in function set(), or a sequence of elements is passed 
in the curly braces and separated by the comma. 
It can contain various types of values. 
'''

set1 = set()
print(type(set1))

set2 = {1, 'Simran', 5, 'Python'}
print(set2)

# Adding element to the set
set2.add(10)
print(set2)

# Removing element from the set
set2.remove(5)
print(set2)

# Dictionary

'''
Dictionary is an unordered set of a key-value pair of items.
But from python 3.6+ means now it is ordered similar to OrderedDict.
The items in the dictionary are separated with the comma (,) and enclosed in the curly braces.
'''

d = {1: 'Jimmy', 2: 'Alex', 3: 'john', 4: 'mike'}

# Printing dictionary
print(d)
print(type(d))

# Accesing value using keys
print("1st name is "+d[1])
print("2nd name is " + d[4])

print(d.keys())           #print all keys
print(d.values())         #print all values

# we will see it in detail in dictionary.py
