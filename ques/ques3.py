#ques 3
# approach 1
sent = input()

#words = sent.strip().split()
# print(len(words))

# approach 2
sent1 = sent.strip()
count = 1
for i in sent1:
    if i == " ":
        count += 1

print(count)
