char_list = list(map(str, input().split()))

for i in range(10) :

    if (i+1) == 2 or (i+1) == 5 or (i+1) == 8 :
        print(char_list[i], end=" ")

