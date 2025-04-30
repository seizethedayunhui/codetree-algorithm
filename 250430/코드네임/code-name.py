class CodeName:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

codename_list = list()
for _ in range(5):
    codename, score = input().split()
    score = int(score)
    codename_list.append(CodeName(codename, score))

min_score = float('inf')
min_index = 0

for i in range(5):
    if codename_list[i].score < min_score :
        min_score = codename_list[i].score
        min_index = i

print(f"{codename_list[min_index].codename} {codename_list[min_index].score}")

    
    