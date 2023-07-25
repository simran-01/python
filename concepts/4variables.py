# python variables

'''
Variable is a name that is used to refer to memory location. 
Python variable is also known as an identifier and used to hold value.
In Python, we don't need to specify the type of variable because it is dynamically typed.
Variable names can be a group of both the letters and digits, but they have to begin with a letter or an underscore.
It is recommended to use lowercase letters for the variable name.

'''

# Rules
# The first character of the variable must be an alphabet or underscore ( _ ).
# All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
# Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
# Identifier name must not be similar to any keyword defined in the language.
# Identifier names are case sensitive; for example, my name, and MyName is not the same.

# Declare and Assign value to variable

'''
We don't need to declare explicitly variable in Python. 
When we assign any value to the variable, that variable is declared automatically.
The equal (=) operator is used to assign value to a variable.
'''

a = 50
b = a   # b will also refer to same int object to which a refers because value is same.

# a and b will have same address
print(a, id(a))
print(b, id(b))

#multi word variables

'''
Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. 
There is no intervention of whitespace. For example - nameOfStudent, valueOfVaraible, etc.
Pascal Case - It is the same as the Camel Case, but here the first word is also capital. 
For example - NameOfStudent, etc.
Snake Case - In the snake case, Words are separated by the underscore. 
For example - name_of_student, etc.
'''

#multiple assignment

#Assigning single value to multiple variables
x=y=z=50    
print(x)    
print(y)    
print(z)    

#Assigning multiple values to multiple variables:
a,b,c=5,10,15    
