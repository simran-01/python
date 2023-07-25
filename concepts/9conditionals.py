
# Conditional statements  - If elif else


'''
---if---
The if statement is used to test a particular condition and if the condition is true, it executes a block of code known as if-block.

--if else--
The if-else statement provides an else block combined with the if statement which is executed in the false case of the condition.
If the condition is true, then the if-block is executed. Otherwise, the else-block is executed.

--elif--
The elif statement enables us to check multiple conditions and execute the specific block of statements depending upon the true condition among them.
We can have any number of elif statements in our program depending upon our need.
However, using elif is optional.
'''

# to check even no
num = int(input("enter the number?"))
if num % 2 == 0:
    print("Number is even")


# to find greatest number of 3 numbers
a = int(input("Enter a? "))
b = int(input("Enter b? "))
c = int(input("Enter c? "))
if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")

# nested if
num = 10
if num == 10:
    if num > 5:
        print("Won")


# if else
age = int(input("Enter your age? "))
if age >= 18:
    print("You are eligible to vote !!")
else:
    print("Sorry! you have to wait !!")


# even or odd
num = int(input("enter the number?"))
if num % 2 == 0:
    print("Number is even...")
else:
    print("Number is odd...")

# if elif else
marks = int(input("Enter the marks? "))
if marks > 85 and marks <= 100:
    print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
    print("You scored grade B + ...")
elif marks > 40 and marks <= 60:
    print("You scored grade B ...")
elif (marks > 30 and marks <= 40):
    print("You scored grade C ...")
else:
    print("Sorry you are fail ?")
