N = int(input())

for i in range(N) :
    num = i+1
    for j in range(N) :
        current_num = 2 * (num+j) + 9
        print(current_num, end=" ")
    print()