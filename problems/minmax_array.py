
def minimum(li):
    small = li[0]
    for i in li:
        if i < small:
            small = i

    return small


def maximum(li):
    large = li[0]
    for i in li:
        if i > large:
            large = i
    return large


li = [2, 4, 5, 6, 8, 9, 1]
print(minimum(li))
print(maximum(li))
