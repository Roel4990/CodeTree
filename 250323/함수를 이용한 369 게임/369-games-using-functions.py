a, b = map(int, input().split())

# Please write your code here.
cnt = 0
def isHaveStr(num):
    num_str = str(num)
    return ("3" in num_str or "6" in num_str or "9" in num_str)

def isThreeMultiple(num):
    return num % 3 == 0

for i in range(a, b+1):
    if (isHaveStr(i) or isThreeMultiple(i)):
        cnt += 1

print(cnt)