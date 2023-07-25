
# Loops
'''
We can run a single statement or set of statements repeatedly using a loop command.
In python we have ..
1. For Loop
2. While Loop
'''

# for loop
'''
Python's for loop is designed to repeatedly execute a code block while iterating through a list, tuple, dictionary, or other iterable objects of Python. 
'''

# for loop in string
str = "Simran"

for i in str:
    print(i)

# for loop in list
lst = ['green', 'red', 'black', 'yellow']


for color in lst:
    print(color)

for i in range(len(lst)):
    print(i)

# print n numbers
for i in range(1, 101):
    print(i)

'''
With the help of the range() function, we may produce a series of numbers. 
We can give specific start, stop, and step size values in the manner range(start, stop, step size).
If the step size is not specified, it defaults to 1.
'''

# odd no from 1 to 10
for i in range(1, 11, 2):
    print(i)

# even no from 1 to 10
for i in range(0, 11, 2):
    if i == 0:
        continue
    print(i)


vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(vowels)):
    print(vowels[i])


# While Loops

'''
While loops are used in Python to iterate until a specified condition is met.
'''
# Python program to show how to use a while loop
counter = 0
# Initiating the loop
while counter < 10:  # giving the condition
    counter = counter + 3
    print("while loop")


# continue , break and pass statement

'''
The continue statement in Python returns the control to the beginning of the while loop.
The break statement in Python terminates the current loop.
Pass statements are used to create empty loops. Pass statement is also employed for classes, functions, and empty control statements.
'''

# Python program to show how the continue statement works

# Initiating the loop
for string in "Python Loops":
    if string == "o" or string == "p" or string == "t":
        continue
    print('Current Letter:', string)


# Python program to show how the break statement works

# Initiating the loop
for string in "Python Loops":
    if string == 'L':
        break
    print('Current Letter: ', string)


# Python program to show how the pass statement works
for string in "Python Loops":
    pass
print('Last Letter:', string)


