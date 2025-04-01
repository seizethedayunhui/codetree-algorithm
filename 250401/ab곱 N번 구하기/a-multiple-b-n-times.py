N = int(input())
ab_list = [list(map(int, input().split())) for _ in range(N)]

for a, b in ab_list :
    mul = 1
    for num in range(a, b+1) :
        mul *= num
    print(mul)
