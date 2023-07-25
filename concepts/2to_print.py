

# - single line comment

'''
multi line comment
'''

# to print anything in python3
print("My name is Simran")

# sep and end and flush arguments
'''
In Python 3, print() is now a function and uses arguments to control its output.
In this lesson, you’ll learn about the sep, end, and flush arguments.
By default, print() inserts a space between the items it is printing. You can change this by using the sep parameter:
Unless told otherwise, print() adds a (\n) at the end of what is being printed. This can be changed with the end parameter. 
Output from print() goes into a buffer. When you change the end parameter, the buffer no longer gets flushed.
To ensure that you get output as soon as print() is called, you also need to use the flush=True parameter:
'''
print("Hello Ms Simran", end=" ", flush=True)

print('Simran', 'Mapari', '21', 'Female', sep="\n")

print("I am an engineer", end=",", flush=True)

print('I', 'Love', 'You', sep='❤️')
