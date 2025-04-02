score_list = list(map(float, input().split()))

score_sum = 0
for score in score_list :
    score_sum += score

score_avg = score_sum / 8
print(f"{score_avg:.1f}")