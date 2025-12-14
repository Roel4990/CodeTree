code, color, second = input().split()

class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

bomb1 = Bomb(code, color, second)

print(f"code : {bomb1.code}\ncolor : {bomb1.color}\nsecond : {bomb1.second}")