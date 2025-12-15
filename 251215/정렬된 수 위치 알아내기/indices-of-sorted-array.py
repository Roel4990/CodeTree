n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
class Position:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value
    
positions = [Position(i, sequence[i]) for i in range(n)]

positions.sort(key = lambda x: x.value)

answer = [0] * n

for new_idx, p in enumerate(positions):
    answer[p.idx] = new_idx + 1

print(*answer)