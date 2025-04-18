n, m = map(int, input().split())
result = []

def recur(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        result.append(i)
        recur(depth + 1)
        result.pop()

recur(0)