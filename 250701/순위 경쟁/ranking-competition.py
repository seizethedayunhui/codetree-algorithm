N = int(input())

ranking = list()
current_ranking = list()

A_score = 0
B_score = 0
C_score = 0


cnt = 0
for _ in range(N) :

    c, s = input().split()
    s = int(s)

    if c == "A" :
        A_score += s
    elif c == "B" :
        B_score += s
    else :
        C_score += s


    # A가 1등인 경우
    if A_score > B_score and A_score > C_score :
        current_ranking = ["A"]
    # B가 1등인 경우
    elif B_score > A_score and B_score > C_score :
        current_ranking = ["B"]
    # C가 1등인 경우
    elif C_score > A_score and C_score > B_score :
        current_ranking = ["C"]
    # A, B
    elif A_score == B_score and A_score > C_score :
        current_ranking = ["A", "B"]
    # A, C
    elif A_score == C_score and A_score > B_score :
        current_ranking = ["A", "C"]
    # B, C
    elif B_score == C_score and B_score > A_score :
        current_ranking = ["B", "C"]
    # A = B = C
    elif A_score == B_score and B_score == C_score :
        current_ranking = ["A", "B", "C"]

    # 개수를 먼저 비교, 그리고 안의 원소 비교
    if len(ranking) == len(current_ranking) :

        flag = True

        for i in range(len(ranking)) :

            if ranking[i] != current_ranking[i] :
                flag = False
                break

        if not flag :
            cnt += 1
        
    else :
        cnt += 1

    ranking = current_ranking

print(cnt)
    





