
# Map , Reduce , Filter , Enumerate , Zip 

#map , filter , reduce
from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(lambda n: n*2, evens))
print(doubles)

sum = reduce(lambda a, b: a+b, doubles)
print(sum)

# enumerate

lst = ["food", "clothes", "vehicle", "shoes"]

for index, item in enumerate(lst):
    if index % 2 == 0:
        print(index, ":", item)

# Zip
names = ['simran', 'arzoo', 'rahul', 'raj', 'darshan']
last_names = ['mapari', 'khan', 'sayyed', 'shaikh', 'rawal']

res = list(zip(names, last_names))  # we can convert to set and dictionary also
print(res)

zipped = zip(names, last_names)
for i, j in zipped:
    print(i, j)
