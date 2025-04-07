word1, word2 = input().split()

if len(word1) > len(word2) :
    print(word1, len(word1))
elif len(word1) == len(word2) :
    print("same")
else :
    print(word2, len(word2))