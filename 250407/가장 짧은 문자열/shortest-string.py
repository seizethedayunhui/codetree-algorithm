min_len = float('inf')
max_len = float('-inf')

for _ in range(3):
    word = input()
    if len(word) > max_len :
        max_len = len(word)
    
    if len(word) < min_len :
        min_len = len(word)

print(max_len-min_len)