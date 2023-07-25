
li = [1, 2, 3, 4, 5, 44, 2, 3, 8]
print(li[::-1])


def rev_array(li):
    rev = []
    for i in range(len(li)-1, -1, -1):
        rev.append(li[i])

    return rev


print(rev_array(li))
