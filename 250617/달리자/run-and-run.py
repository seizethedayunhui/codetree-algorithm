N = int(input())

original = list(map(int, input().split()))
final = list(map(int, input().split()))

cnt = 0
# 뒤에서부터 가장 끝으로 옮김.
for i in range(N) :
    if original[i] > final[i] :
        gap = abs(original[i] - final[i])
        for j in range(N-1, -1, -1) :

            if final[j] > original[j] :
                
                current_gap = abs(original[j] - final[j])
                cnt += (gap * (j-i) )

                if current_gap >= gap :
                    original[j] += gap
                    gap = 0               
                    break

                else :
                    original[j] += current_gap
                    gap = abs(gap-current_gap)

print(cnt)
                
                
                
        




            

        

    
