word_list = ["apple", "banana", "grape", "blueberry", "orange"]
char = input()

cnt = 0

for word in word_list :
    if word[2] == char or word[3] == char :
        print(word)
        cnt += 1
print(cnt)