n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
current_pos = 0
segments = {}

for dist, d in zip(x, dir):
    if d == 'R':
        for i in range(current_pos, current_pos + dist):
            segments[i] = segments.get(i, 0) + 1
        current_pos += dist
    else:
        for i in range(current_pos - dist, current_pos):
            segments[i] = segments.get(i, 0) + 1
        current_pos -= dist

answer = 0
for count in segments.values():
    if count >= 2:
        answer += 1

print(answer)