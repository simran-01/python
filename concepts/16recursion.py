# Recursion - Function calls itself

import sys

print(sys.getrecursionlimit())  # by default it is 1000
print(sys.setrecursionlimit(2000))  # we can set it to any number

# Factorial using Recursion


def fact(num):
    if num == 0:     # base or stop condition
        return 1

    return num * fact(num-1)  # calling itself


print(fact(5))
