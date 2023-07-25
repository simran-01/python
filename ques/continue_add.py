

def loop_add(num):
    while (len(str(num)) > 1):
        strr = str(num)
        digit_list = list(map(int, strr.strip()))
        num = sum(digit_list)

    return num


print(loop_add(38))
