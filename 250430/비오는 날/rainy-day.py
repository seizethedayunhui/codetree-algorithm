class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
ans_list = list()

for _ in range(n):
    date, day, weather = input().split()
    # 계산의 편리성을 위해 split 해서 저장

    if weather == "Rain":
        ans_list.append(Weather(date, day, weather))

ans_list.sort(key= lambda x : x.date)

print(f"{ans_list[0].date} {ans_list[0].day} {ans_list[0].weather}")

# y = float('inf')
# m = float('inf')
# d = float('inf')

# near = Weather((y, m, d), None, None)

# for elem in ans_list :
#     if elem.date[0] < near.date[0] :
#         near = elem
#     elif elem.date[0] == near.date[0] :
#         if elem.date[1] < near.date[1] :
#             near = elem
#         elif elem.date[1] == near.date[1] :
#             if elem.date[2] < near.date[2] :
#                 near = elem

# print(f"{near.date[0]}-{near.date[1]}-{near.date[2]} {near.day} {near.weather}")



    
