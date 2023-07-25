

def merge_sorted_array(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res = res + arr1[i:] + arr2[j:]
    return res


print(merge_sorted_array([2, 3, 8, 15], [1, 10, 11, 19]))



