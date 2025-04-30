class Info:
    def __init__(self, id_info = "codetree", level_info = 10):
        self.id_info = id_info
        self.level_info = level_info

user1 = Info()

input_id, input_level = input().split()
user2 = Info(input_id, int(input_level))

print(f"user {user1.id_info} lv {user1.level_info}")
print(f"user {user2.id_info} lv {user2.level_info}")