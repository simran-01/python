

def norepeatation(input_list):
    new_list = []
    for i in input_list:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(norepeatation([1, 2, 3, 2, 1, 5, 6, 7, 3]))
