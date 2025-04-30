class Info:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

info_list = list()

n = int(input())
for _ in range(n):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    info_list.append(Info(name, kor, eng, math))

info_list.sort(key= lambda x : (-x.kor, -x.eng, -x.math))

for info in info_list:
    print(f"{info.name} {info.kor} {info.eng} {info.math}")