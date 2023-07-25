
def gcd(a, b):
    if a < b:
        while (a != b):
            b = b-a
    else:
        while (a != b):
            a = a-b
    return a


print(gcd(15, 60))


def lcm(a, b):
    return a*b/gcd(a, b)


print(lcm(15, 60))
