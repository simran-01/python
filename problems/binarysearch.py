
def binary_search(li, key):
    l = 0
    h = len(li)-1

    while l <= h:
        mid = (l + h) // 2

        if li[mid] == key:
            print("found at index", mid)
            return 1

        if li[mid] > key:
            h = mid-1

        elif li[mid] < key:
            l = mid+1

    return -1


binary_search([1, 4, 6, 8, 9, 10], 9)
