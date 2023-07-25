
# fibonacci series  - normal

def fibonacci(num):
    a, b = 0, 1
    print(a, b, end=" ")
    for i in range(num-2):
        c = a+b
        print(c, end=" ")
        a, b = b, c


fibonacci(5)




#for particular no of series, start from 1 index
def fibonacci_recursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

num=int(input("enter: "))
print(fibonacci_recursive(num))

