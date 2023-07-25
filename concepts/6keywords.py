
# Keywords
'''
Every language has designated words or keywords, with particular definitions and usage guidelines.
Python keywords are unique words reserved with defined meanings and functions that we can only apply for those functions.
You'll never need to import any keyword into your program because they're permanently present.

'''

'''
In distinct versions of Python, the preceding keywords might be changed.
Some extras may be introduced, while others may be deleted. 
By writing the following statement into the coding window, you can anytime retrieve the collection of keywords in the version you are working on.
'''

# Python program to demonstrate the application of iskeyword()
# importing keyword library which has lists

# displaying the complete list using "kwlist()."
import keyword
print("The set of keywords in this version is: ")
print(keyword.kwlist)

# By calling help(), you can retrieve a list of currently offered keywords:
help('keywords')


#we will be using many keywords further.