N = int(input())

num_list = list()

def solution(N, cnt, num_list) :

    if N == cnt :
        return num_list[N-1]

    if cnt == 0 :
        num_list.append(1)
    elif cnt == 1 :
        num_list.append(2)
    else :
        ans = num_list[ (cnt+1)//3-1 ] + num_list[ cnt-1 ]
        num_list.append(ans)

    return solution(N, cnt+1, num_list)

print(solution(N, 0, num_list))