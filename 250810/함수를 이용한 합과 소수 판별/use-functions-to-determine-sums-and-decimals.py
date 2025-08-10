a, b = map(int, input().split())

# Please write your code here.
def is_prime_number(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

cnt = 0
for i in range(a, b + 1):
    if is_prime_number(i):
        if sum(map(int, str(i))) % 2 == 0:
            cnt += 1

print(cnt)
