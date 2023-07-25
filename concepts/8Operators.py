
# Operators
'''
The operator can be defined as a symbol which is responsible for a particular operation between two operands. 
Operators are the pillars of a program on which the logic is built in a specific programming language.
Python provides a variety of operators, which are described as follows.

1.Arithmetic operators
2.Comparison operators
3.Assignment Operators
4.Logical Operators
5.Bitwise Operators
6.Membership Operators
7.Identity Operators
'''

# Arithmetic
'''
Arithmetic operators are used to perform arithmetic operations between two operands.
It includes + (addition), - (subtraction), *(multiplication), /(divide), %(reminder), //(floor division), 
and exponent (**) operators.
'''

a = 10
b = 5

print(a+b, a*b, a-b, a % b, a/b, a//b, a**b, sep="\n")

# Comparison
'''
Comparison operators are used to comparing the value of the two operands and returns Boolean true or false accordingly.
1. ==
2. !=
3. >
4. <
5. >=
6. <=
'''

print(a == b, a != b, a > b, a < b, a >= b, a <= b, sep="\n")

# Assignment
'''
The assignment operators are used to assign the value of the right expression to the left operand.
'''

x = 20  # assign value 20 to a
print(x)

x += 5  # adding value 5 in x  - x = x+5
print(x)

x -= 2  # substracting 2 from x - x = x-2
print(x)

x *= 10  # multiply 10 in x - x= x*10
print(x)

x %= 5        # x = x%5
print(x)

x **= 2      # x = x**2
print(x)

# Logical
'''
The logical operators are used primarily in the expression evaluation to make a decision.
1. and
2. or
3. not
'''

a = True
b = False

print(a and b, a or b, not (a))

# Identity
'''
The identity operators are used to decide whether an element certain class or type.
1. is - It is evaluated to be true if the reference present at both sides point to the same object.
2. is not - It is evaluated to be true if the reference present at both sides do not point to the same object.
'''

a = 5
b = a
c = 10

print(a is b)
print(a is not b)
print(a is not c)


# Membership
'''
Python membership operators are used to check the membership of value inside a Python data structure.
If the value is present in the data structure, then the resulting value is true otherwise it returns false.
1. in - It is evaluated to be true if the first operand is found in the second operand (list, tuple, or dictionary).
2. in not - It is evaluated to be true if the first operand is not found in the second operand (list, tuple, or dictionary).
'''
num_list = [1, 2, 6, 8, 4, 10]

print(2 in num_list)
print(3 in num_list)
print(3 not in num_list)

# Bitwise
'''
The bitwise operators perform bit by bit operation on the values of the two operands.
1. ~ (negation / complement) - It calculates the negation of each bit of the operand, i.e., if the bit is 0, the resulting bit will be 1 and vice versa.
2. & - AND (If both the bits at the same place in two operands are 1, then 1 is copied to the result. Otherwise, 0 is copied.)
3. | - OR  (The resulting bit will be 0 if both the bits are zero; otherwise, the resulting bit will be 1.)
4. ^ - XOR (The resulting bit will be 1 if both the bits are different; otherwise, the resulting bit will be 0.)
5. >> - right shift (The left operand is moved right by the number of bits present in the right operand.)
6. << - left shift (The left operand value is moved left by the number of bits present in the right operand.)
'''

a = 12
b = 13
print(~a)
print(a & b)
print(a | b)
print(a ^ b)


# left shift - we gain bits and right shift - we lose bits
x = 10
y = 2

print(x >> y)
print(x << y)
