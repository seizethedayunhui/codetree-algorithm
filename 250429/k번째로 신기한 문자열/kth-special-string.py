N, K, T = input().split()

N = int(N)
K = int(K)

T_words = list()

for _ in range(N) :

    word = input()

    if word[:len(T)] == T :
        T_words.append(word)

T_words.sort()

print(T_words[K-1])

