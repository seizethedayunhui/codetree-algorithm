first, second = map(int, input().split())

for i in range(10) :
    if i == 0 :
        print(first, end=" ")
        continue
    elif i == 1 :
        print(second, end=" ")
        continue
    ans = (first + second) % 10
    first = second
    second = ans
    print(ans, end=" ")