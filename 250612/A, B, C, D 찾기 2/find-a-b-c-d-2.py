arr = list(map(int, input().split()))
arr.sort()

for A in range(1, 41) :
    for B in range(A, 41) :
        for C in range(B, 41) :
            for D in range(C, 41) :
                
                picks = [ A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D] 
                picks.sort()

                flag = True

                for picks_elem, arr_elem in zip(picks, arr) :
                    if picks_elem != arr_elem :
                        flag = False
                        break

                if flag :
                    print(A, B, C, D)