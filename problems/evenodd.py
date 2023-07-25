
def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


# 1122  count even odd

def count_even_odd(num):
    even_count = 0
    odd_count = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f"Even={even_count} Odd={odd_count}"


print(count_even_odd(1122))
