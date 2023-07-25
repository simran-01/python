
#Exceptions
# try:  
#     # Code block  
#     # These statements are those which can probably have some error  
  
# except:  
#     # This block is optional.  
#     # If the try block encounters an exception, this block will handle it.  
  
# else:  
#     # If there is no exception, this code block will be executed by the Python interpreter  
  
# finally:  
#     # Python interpreter will always execute this code.  

a = 5
b = 2

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero" , e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print("resource Closed")