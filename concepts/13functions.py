
# Functions

'''
Python Functions is a block of statements that return the specific task.
The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing
the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again. 

Benefits:
1.By including functions, we can prevent repeating the same code block repeatedly in a program.
2.Python functions, once defined, can be called many times and from anywhere in a program.
3.If our Python program is large, it can be separated into numerous functions which is simple to track.
4.The key accomplishment of Python functions is we can return as many outputs as we want with different arguments.

Two types:
1. Built in 
2. User defined
'''

# syntax


def name_of_function(parameters):
    """This is a docstring"""
    # code block

# documentation string called docstring in the short form is to explain the purpose of the function.

# example


def square(num):
    """
    This function computes square of number
    """
    sq = num ** 2

    return sq


ans = square(2)    # call function passing argument i.e 2

# returned value by fxn will be stored in ans

print(ans)

# In the Python programming language, all arguments are supplied by reference.
# It implies that if we modify the value of an argument within a function,
# the change is also reflected in the calling function.


def my_function(lst):
    lst.append(2)

    return lst


lst1 = [1, 4, 6, 8]

print(my_function(lst1))

print(lst1)  # original lst1 is also changed

# Types of arguments
"""
1.Default 
2.keyword
3.Required
4.Variable-length
"""
# A default argument is a kind of parameter that takes as input a default value
# if no value is supplied for the argument when the function is called.

# Python code to demonstrate the use of default arguments
# defining a function


def function(num1, num2=40):
    print("num1 is: ", num1)
    print("num2 is: ", num2)


# Calling the function and passing only one argument
print("Passing one argument")
function(10)

# Now giving two arguments to the function
print("Passing two arguments")
function(10, 30)

# keyword


def person(name, age):
    print(name)
    print(age+5)


person(age=21, name='simran')

# Variable length
'''
We can use special characters in Python functions to pass as many arguments as we want in a function. 
There are two types of characters that we can use for this purpose:
*args -These are Non-Keyword Arguments
**kwargs - These are Keyword Arguments.
'''

# args


def sum(*args):  # it will accept argument in tuple(we can name args anything)
    c = 0
    for i in args:
        c += i

    return c


print(sum(1, 4, 5, 7, 2))  # we can pass as many arguments we want


# kwargs

def person(**kwargs): # accepts it in dictionary
    for key, value in kwargs.items():
        print(key, ":", value)


person(name="simran", age=21, city="Mumbai", mob=913612345) #passing multiple arguments with keywords
