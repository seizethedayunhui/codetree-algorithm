N = int(input())
score_list = [ list(map(int, input().split())) for _ in range(N) ]

# 패스한 학생 수를 카운트 하는 변수
student_cnt = 0

for scores in score_list :
    score_sum = 0
    for score in scores :
        score_sum += score
    score_avg = score_sum / 4

    if score_avg >= 60 :
        print("pass")
        student_cnt += 1
    else :
        print("fail")

print(student_cnt)