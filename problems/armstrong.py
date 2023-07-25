
# armstrong

def armstrong(num):
    sum = 0
    temp = num
    while (temp > 0):
        a = temp % 10
        sum = sum + a ** len(str(num))
        temp = temp // 10

    if sum == num:
        return "It is Armstrong number"
    else:
        return "Not a Armstrong"


print(armstrong(153))
