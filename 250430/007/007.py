class Secret:
    def __init__(self, code, where, when):
        self.code = code
        self.where = where
        self.when = when

code, where, when = input().split()
Secret_code = Secret(code, where, when)

print(f"secret code : {Secret_code.code}")
print(f"meeting point : {Secret_code.where}")
print(f"time : {Secret_code.when}")