N = int(input())
lst = []
for i in range(1, N+1):
    command = input()
    cmd_list = command.split(" ")
    if cmd_list[0] == "insert":
        lst.insert(int(cmd_list[1]), int(cmd_list[2]))
    elif cmd_list[0] == "print":
        print(lst)
    elif cmd_list[0] == "remove":
        lst.remove(int(cmd_list[1]))
    elif cmd_list[0] == "append":
        lst.append(int(cmd_list[1]))
    elif cmd_list[0] == "sort":
        lst.sort()
    elif cmd_list[0] == "pop":
        lst.pop()
    elif cmd_list[0] == "reverse":
        lst.reverse()
