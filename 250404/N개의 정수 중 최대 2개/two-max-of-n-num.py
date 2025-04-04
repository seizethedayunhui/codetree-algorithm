N = int(input())
num_list = list(map(int, input().split()))

max_1st = float('-inf')
max_2nd = float('-inf')

for num in num_list :
    if num > max_1st :
        max_1st = num
    elif num > max_2nd :
        max_2nd = num   
    
print(f"{max_1st} {max_2nd}")
    
