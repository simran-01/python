
# how to take input from user - input()
# It always considers input value as string so for other operations you need to typecast


a = input("Enter your age: ")
print(type(a))  # type() is used to check data type
print(a)

# typecast

b = int(input("What is your current salary?"))  # int() will convert str to int
print(type(b), b)
