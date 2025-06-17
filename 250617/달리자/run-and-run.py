N = int(input())

original = list(map(int, input().split()))
final = list(map(int, input().split()))

cnt = 0
# 뒤에서부터 가장 끝으로 옮김.
for i in range(N-1) :
    if original[i] > final[i] :
        gap = abs(original[i] - final[i])

        next_gap = abs(original[i+1] - final[i+1])

        cnt += (gap)

        original[i+1] += gap

print(cnt)
                
                
                
        




            

        

    
