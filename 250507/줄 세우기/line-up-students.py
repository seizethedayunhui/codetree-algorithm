class Student:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n


N = int(input())

Students = list()
for i in range(N):

    h, w = map(int, input().split())
    Students.append(Student(h, w, i+1))

# 정렬하기 (키, 몸무게 내립차순)
Students.sort(key= lambda x : (-x.h, -x.w))

for student in Students:
    print(f"{student.h} {student.w} {student.n}")




