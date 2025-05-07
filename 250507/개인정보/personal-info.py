class Human:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h 
        self.w = w

Human_list = list()

for _ in range(5):
    name, h, w = input().split()
    Human_list.append(Human(name, int(h), float(w)))


Human_list.sort(key = lambda x : x.name)

print("name")
for human in Human_list:
    print(f"{human.name} {human.h} {human.w}")

Human_list.sort(key = lambda x : -x.h)

print()
print("height")
for human in Human_list:
    print(f"{human.name} {human.h} {human.w}")