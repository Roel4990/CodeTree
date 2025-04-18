n = int(input())

# Please write your code here.
result = []
cnt = 0

def is_beautiful(s):
    i = 0
    while i < len(s):
        num = int(s[i])
        if i + num > len(s):
            return False
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
    for i in range(1, 10):  # 1부터 9까지 사용
        recur(current + str(i))

recur('')
print(cnt)