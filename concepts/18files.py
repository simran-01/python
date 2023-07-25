
# Files I/O

'''
file operation can be done in the following order.
Open a file
Read or write - Performing operation
Close the file

Python provides an open() function that accepts two arguments, file name and access mode 
in which the file is accessed. The function returns a file object which can be used to perform 
various operations like reading, writing, etc.
'''

f = open("simran.txt", "rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()

# f = open("simran.txt", "w")
# a = f.write("hum bahut achhe hain\n")
# print(a)
# f.close()

# f = open("simran.txt", "a")
# a = f.write("hum bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("simran.txt", "r+")
print(f.read())
f.write("thank you")

#seek and tell
'''
the tell() function. f.tell() returns an integer giving the file pointer current position in the file represented as a number of bytes. File Pointer/File Handler is like a cursor, which defines from where the data has to be read or written in the file. Sometimes it becomes important for us to know the position of the File Pointer.
With the help of tell(), this task can be performed easily.

seek is used to change file pointer position
'''
f = open("simran.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
  

#with block to open file 
with open("simran.txt") as f:
    a = f.readlines()
    print(a)
