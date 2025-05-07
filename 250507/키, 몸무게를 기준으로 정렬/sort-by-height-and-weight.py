class Human:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h 
        self.w = w

n = int(input())
Human_list = list()

for _ in range(n):
    name, h, w = input().split()
    Human_list.append(Human(name, int(h), int(w)))

Human_list.sort(key = lambda x : (x.h, -x.w))

for human in Human_list:
    print(f"{human.name} {human.h} {human.w}")