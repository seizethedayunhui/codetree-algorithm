number = [ int(input()) for _ in range(5) ]

cnt = 0
for num in number :
    if num % 2 == 0 :
        cnt += 1

print(cnt)