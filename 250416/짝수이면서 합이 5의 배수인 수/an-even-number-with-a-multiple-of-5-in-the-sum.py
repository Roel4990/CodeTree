n = int(input())

# Please write your code here.
def is_magic_number(i):
    return i % 2 == 0 and sum(list(map(int, str(i)))) % 5 == 0

print("Yes" if is_magic_number(n) else "No")
