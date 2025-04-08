N = int(input())

word_list = list()

for _ in range(N) :
    word_list.append(input())

char = input()

cnt = 0
len_sum = 0

for word in word_list :
    if word[0] == char :
        cnt += 1
    len_sum += len(word)

word_len_avg = len_sum // N

print(f"{cnt} {word_len_avg:.2f}")