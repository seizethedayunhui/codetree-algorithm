word_list = list()

for _ in range(10) :
    word_list.append(input())

char = input()

flag = 0

for i in range(10) :
    if word_list[i][-1] == char :
        flag = 1
        print(word_list[i])

if not flag :
    print("None")