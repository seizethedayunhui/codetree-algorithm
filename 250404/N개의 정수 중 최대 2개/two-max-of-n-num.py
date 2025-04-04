N = int(input())
num_list = list(map(int, input().split()))

max_1st = float('-inf')
max_2nd = float('-inf')

for num in num_list :
    if num > max_1st :

        # max_1st 이던 값을 max_2nd로 정정해주어야함. 
        # 해주지 않으면 원소가 2개인 경우 에러남. 
        max_2nd = max_1st
        max_1st = num

    elif num > max_2nd :
        max_2nd = num   
    
print(f"{max_1st} {max_2nd}")
    
