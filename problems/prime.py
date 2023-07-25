
def prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                print("not prime")
                break
        else:
            print("prime number")

    else:
        print("not a prime")


prime(0)
