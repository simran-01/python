
# reverse

# loop
def reverse(input_str):
    rev = ""
    for i in input_str:
        rev = i + rev

    return rev


print(reverse("simran"))


# slicing
text = "Hello"
print(text[::-1])

# number reverse

num = 1010
reverse = str(num)[::-1]
print(reverse)

# other

num = 123
rev = 0

while (num > 0):
    a = num % 10
    rev = rev*10 + a
    num = num//10

print(rev)
