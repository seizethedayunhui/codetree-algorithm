a, b, c = map(int, input().split())

# a와 b를 비교한뒤, a가 b보다 크다면 a와 c를 비교하여 최댓값을 구합니다.
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)

# a와 b를 비교한 결과가 나와있으므로, b와 c만 비교하여 최댓값을 구합니다.
else:
    if b >= c:
        print(b)
    else:
        print(c)