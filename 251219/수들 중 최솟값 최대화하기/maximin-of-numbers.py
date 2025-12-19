N = int(input())
mat = [ list(map(int, input().split())) for _ in range(N) ]

rows = [ False for _ in range(N) ]
cols = [ False for _ in range(N) ]

def find_max_min_element(current_min_element, idx, cnt) :

    if cnt == N :
        return current_min_element
    
    if ( idx == N or rows[idx] ) :
        return -1

    max_min_element = float('-inf')
    
    rows[idx] = True

    for j in range(N) :

        if cols[j] :
            continue

        cols[j] = True
        element = min(current_min_element, mat[idx][j])
        max_min_element = max(max_min_element, find_max_min_element(element, idx+1, cnt+1))
        cols[j] = False
    
    rows[idx] = False

    return max_min_element

ans = find_max_min_element(float('inf'), 0, 0)
print(ans)