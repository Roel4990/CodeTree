n = int(input())

# Please write your code here.
cnt = 0

def recur(current, length):
    global cnt
    if length == n:
        cnt += 1
        return
    if length > n:
        return

    for i in range(1, 10):
        group = str(i) * i
        recur(current + group, length + i)

recur('', 0)
print(cnt)