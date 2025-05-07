class Student :
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n

N = int(input())

Student_list = list()

for i in range(N):
    h, w = map(int, input().split())

    Student_list.append(Student(h, w, i+1))

Student_list.sort(key = lambda x : (x.h, -x.w))

for student in Student_list:
    print(f"{student.h} {student.w} {student.n}")