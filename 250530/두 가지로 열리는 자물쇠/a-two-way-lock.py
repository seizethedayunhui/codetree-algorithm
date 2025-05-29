N = int(input())
comb1 = list(map(int, input().split()))
comb2 = list(map(int, input().split()))

def calc_dis(elem1, elem2, N) :

    if elem1 > elem2 :
        return min(abs(elem1 - elem2), abs((elem1-N)-elem2))
    elif elem2 > elem1 :
        return min(abs(elem2 - elem1), abs((elem2-N)-elem1))
    else :
        return 0

def calc_flag(comb1, comb2, N) :

    comb_flag = True

    for i in range(3) :

        if calc_dis(comb1[i], comb2[i], N) > 2 :
            comb_flag = False
            break

    return comb_flag


cnt = 0

for i in range(N):
    for j in range(N) :
        for k in range(N) :

            comb = [ i+1, j+1, k+1]

            if calc_flag(comb, comb1, N) or calc_flag(comb, comb2, N):
                    cnt += 1

            # if calc_flag(comb, comb1, N) and calc_flag(comb, comb2, N):
            #     print("겹치는 경우", comb, comb1, comb2)
            # elif calc_flag(comb, comb1, N):
            #     print("조합1과 만족", comb, comb1)
            # elif calc_flag(comb, comb2, N):
            #     print("조합2와 만족", comb, comb2)
print(cnt)