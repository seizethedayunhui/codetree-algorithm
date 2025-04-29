word1 = list(input())
word2 = list(input())

word1.sort()
word2.sort()

flag = True


for i in range(len(word1)):

    if word1[i] != word2[i] or len(word1) != len(word2) :
        flag = False
        break

if flag :
    print("Yes")
else :
    print("No")

    