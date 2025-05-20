a = list(input())

a_len = len(a)

for i in range(a_len) :
    a[i] = int(a[i])

max_N = float('-inf')

for i in range(1, a_len) :

    a_sum = 0

    if a[i] == 0 :
        a[i] += 1
    else :
        a[i] -= 1

    for j in range(a_len) :
            a_sum += (2 ** (a_len-(j+1))) * a[j]

    if a[i] :
        a[i] -= 1
    else :
        a[i] += 1

    max_N = max(max_N, a_sum)

print(max_N)

