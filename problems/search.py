

def search(key, li):
    flag = 0
    for i in range(len(li)):
        if li[i] == key:
            print(key, "is present at index", i)
            flag = 1
            break
    if flag == 0:
        print("not found")


li = [1, 4, 6, 7, 3, 2]
search(9, li)
