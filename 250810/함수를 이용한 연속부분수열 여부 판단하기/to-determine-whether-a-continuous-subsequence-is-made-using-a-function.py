n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def addWord(nums):
    return ''.join(map(str, nums))
if n2 > n1:
    print("No")
else:
    print("Yes" if addWord(b) in addWord(a) else "No")
    