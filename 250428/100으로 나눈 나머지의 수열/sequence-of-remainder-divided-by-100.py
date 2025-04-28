N = int(input())

num_list = list()

def solution(N, num_list, cnt) :

    if cnt == N :
        return num_list[cnt-1]
    
    if cnt == 0 :
        num_list.append(2)
    elif cnt == 1 :
        num_list.append(4)
    else :
        ans = (num_list[cnt-2] * num_list[cnt-1]) % 100
        num_list.append(ans)
    return solution(N, num_list, cnt+1)
    
print(solution(N, num_list, 0))