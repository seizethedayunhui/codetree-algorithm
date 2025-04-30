class BombInfo:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()
new_bomb = BombInfo(code, color, sec)

print(f"code : {new_bomb.code}")
print(f"color : {new_bomb.color}")
print(f"second : {new_bomb.sec}")