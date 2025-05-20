a = list(input())

a_len = len(a)

for i in range(a_len) :
    a[i] = int(a[i])

max_N = float('-inf')

for i in range(a_len) :

    a_sum = 0

    for j in range(a_len) :
        if (i != j) :
            a_sum += (2 ** (a_len-(j+1)))

    max_N = max(max_N, a_sum)

print(max_N)

