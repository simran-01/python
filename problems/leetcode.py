
# leetcode 1470 - shuffle  array
# nums = [2,5,1,3,4,7]
# n=3

# x_values= nums[:n]
# y_values=nums[n:]
# shuffle_list = []

# for x , y in zip(x_values,y_values):
#     shuffle_list.append(x)
#     shuffle_list.append(y)


# print(shuffle_list)

# leetcode
# n= 234
# sum = 0
# prod = 1

# while(n>0):
#     sum+=n%10
#     prod*=n%10
#     n=n//10

# print(prod-sum)

# 215 kth largest not distinct

# descending
# nums = [3,2,1,5,6,4]
# k = 2

# nums.sort(reverse=True)
# print(nums[k-1])

# ascending
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4

# nums.sort()
# print(nums[-k])

# 744. Find Smallest Letter Greater Than Target

# letters = ["x","x","y","y"]
# target = 'z'
# flag=0

# for i in letters:
#     if i > target:
#         print(i)
#         flag=1
#         break

# if flag==0:
#     print(letters[0])


# Two sum

# nums = [2,7,11,15]
# target = 9

# sum = 0
# lst= []


# fibonacci
# 0 1 1 2 3 5 8

# def fibo(n):
#     fibo_lst = [0 , 1 , 1]

#     for i in range(n-2):
#         c = fibo_lst[i+1]+fibo_lst[i+2]
#         fibo_lst.append(c)

#     return fibo_lst[n]

# print(fibo(6))

# Two sum

# nums = [2,5,5,11]
# target = 10

# for i in range(len(nums)):
#     for j in range(1,  len(nums)):
#         if nums[i]+nums[j] == target:
#             print(i, j)


# i = 0 j = 1

# def twosum(nums,target):
#      for i in range(len(nums)):
#         for j in range(1,  len(nums)):
#             if nums[i]+nums[j] == target:
#                 return i,j


# print(twosum([2,5,5,11],10))

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# wrong
# def add_repeat(num):

#     sum = 0
#     while (num > 0):
#         sum += num % 10
#         num = num//10

#     if sum<=9:
#         return sum

#     if sum > 9:
#         add_repeat(sum)


# print(add_repeat(38))

# def digSum( n):
#     sum = 0

#     while(n > 0 or sum > 9):

#         if(n == 0):
#             n = sum
#             sum = 0

#         sum += n % 10
#         n /= 10

#     return sum

# Driver method
# n = 1234
# print (digSum(n))

# def digSum(n):

#     if (n == 0):
#         return 0
#     if (n % 9 == 0):
#         return 9
#     else:
#        return (n % 9)


# n = 9999
# print(digSum(n))

# a = '11'
# b='1'

# ans = bin(int(a,2)+int(b,2))

# print(ans[2:])

num = [2, 7, 4]
k = 181

num1 = ''
for i in num:
    num1 += str(i)
add = int(num1)+k
res = list(map(int, [x for x in str(add)]))
print(res)
