# def my_function(lst):
#     lst.append(2)

#     return lst

# lst1 = [1, 4, 6, 8]

# print(my_function(lst1))

# print(lst1)

# n = int(input())

# lst = map(int , input().split())

# # input
# records = []
# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append([name, score])

# # get second max score
# scores = []
# for entry in records:
#     scores.append(entry[1])
# scores.sort()
# second_max = scores[2]

# # list of names with second max score
# second_max_list = []
# for entry in records:
#     if entry[1] == second_max:
#         second_max_list.append(entry)

# # sort alphabetically
# second_max_list.sort()
# for i in second_max_list:
#     print(i[0])

# lst = [['simran',30],['muskan',20],['zikra',10],['rabiya',5]]

# lst.sort()
# print(lst)

# lst = [5,3,6,1,4,2]
# lst.sort()

# for i in range(len(lst)):
#     print(lst[i])

# s = '({})'

# dic={')':'(','}':'{',']':'['}
# stack = []


# for p in s:
#     if p in dic.values():
#         stack.append(p)

#     if p in dic.keys():
#         if stack[-1]==dic[p]:
#             stack.pop()
#         else:
#             print("False")
#             break


# if stack == []:
#     print("True")
# else:
#     print("False")


# 217

# #nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]

# if len(nums)!=len(set(nums)):
#     print('true')
# else:
#     print('false')

# 136. Single Number

# 121

# prices = [7, 6, 4, 3, 1]
# prices = [7,1,5,3,6,4]


# def stock(prices):
#     if (prices == sorted(prices, reverse=True)):
#         return 0

#     else:
#         buy_price = min(prices)
#         buy_day = prices.index(buy_price)

#         sell_price = max(prices[buy_day+1:])

#         return (sell_price-buy_price)


# print(stock([7,6,4,3,1]))

# 58 length of last word

# s = "   fly me   to   the moon  "

# a = list(" ".join(s.strip().split()).split())

# print( len(a[-1]))
# s = "   fly me   to   the moon  "

# a= s.split()
# print(a)
# print(len(a[-1]))

# 1351. Count Negative Numbers in a Sorted Matrix

# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

# count = 0

# for i in grid :
#     for j in i :
#         if j<0:
#             count+=1

# print(count)

# 1346. Check If N and Its Double Exist

#arr = [3,1,7,11]
# arr=[-2,0,10,-19,4,6,-8]

# for i in range(len(arr)):
#     if arr[i]*2 in (arr[:i]+arr[i+1:]):
#         print('true')

# reverse
# s = "  hello world  "
# a=s.strip().split()[::-1]
# str1= ' '.join(map(str, a))
# print(str1)

nums = [5,2,3,1]
nums.sort()

print(nums)