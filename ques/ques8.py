#ques8
no = input()
even_sum = 0
odd_sum = 0

for i in no:
    if int(i) % 2 == 0:
        even_sum += int(i)
    else:
        odd_sum += int(i)

print(odd_sum-even_sum)
