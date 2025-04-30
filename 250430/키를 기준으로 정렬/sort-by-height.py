class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
info_list = list()

for _ in range(n) :
    name, height, weight = input().split()
    height = int(height)
    weight = int(weight)
    info_list.append(Info(name, height, weight))

info_list.sort(key= lambda x : x.height)

for info in info_list :
    print(f"{info.name} {info.height} {info.weight}")