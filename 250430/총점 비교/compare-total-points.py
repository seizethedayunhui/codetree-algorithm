class Score:
    def __init__ (self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

N = int(input())

score_list = list()
for _ in range(N):
    name, score1, score2, score3 = input().split()
    score_list.append(Score(name, int(score1), int(score2), int(score3)))

score_list.sort(key= lambda x : (x.score1 + x.score2 + x.score3))

for score in score_list :
    print(f"{score.name} {score.score1} {score.score2} {score.score3}")