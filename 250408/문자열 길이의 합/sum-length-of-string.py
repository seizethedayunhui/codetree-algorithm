n = int(input())

cnt_len = 0
cnt_a = 0
for _ in range(n) :
    word = input()
    if word[0] == 'a' :
        cnt_a += 1
    cnt_len += len(word)

print(cnt_len, cnt_a)