N = int(input())

score_list = list(map(float, input().split()))
score_sum = 0

for score in score_list :
    score_sum += score

score_avg = score_sum / N

print(f"{score_avg:.1f}")

if score_avg >= 4.0 :
    print("Perfect")
elif score_avg >= 3.0 :
    print("Good")
else :
    print("Poor")