n = int(input())

# Please write your code here.
result = []
cnt = 0

def is_beautiful(s):
    i = 0
    while i < len(s):
        num = int(s[i])
        # 현재 숫자가 num번 연속되는지 확인
        if s[i:i+num] != s[i] * num:
            return False
        i += num
    return i == len(s)

def recur(current):
    global cnt
    if len(current) == n:
        if is_beautiful(current):
            cnt += 1
        return
    for i in range(1, 10):
        recur(current + str(i))

recur('')
print(cnt)