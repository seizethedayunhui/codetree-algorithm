N = int(input())

def print_square(N) :
    cnt = 1
    for _ in range(N) :
        for _ in range(N) :
            if cnt > 9 :
                cnt = 1
            print(cnt, end=" ")
            cnt += 1
        print()

print_square(N)
        