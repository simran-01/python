#ques10
n = int(input())
lst = [int(i) for i in input().split()][:n]

min = lst[0]
max = lst[0]

for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]
    elif lst[i] > max:
        max = lst[i]

print(min+max)
