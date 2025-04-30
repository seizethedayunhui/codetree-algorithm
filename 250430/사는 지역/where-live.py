class Info:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location

info_list= list()

n = int(input())
for _ in range(n):
    name, address, location = input().split()
    info_list.append(Info(name, address, location))

info_list.sort(key= lambda x : x.name, reverse=True)

print(f"name {info_list[0].name}")
print(f"addr {info_list[0].address}")
print(f"city {info_list[0].location}")

