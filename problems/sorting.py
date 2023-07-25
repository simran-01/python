# bubble sort

# ascending

def sort_ascending(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


print(sort_ascending([2, 5, 6, 7, 1, 3]))

# descending


def sort_descending(num):
    for i in range(len(num)-1, 0, -1):
        for j in range(i):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num


print(sort_descending([1, 2, 3, 4, 6, 8, 9]))
