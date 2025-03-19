mathA, englishA = map(int, input().split())
mathB, englishB = map(int, input().split())

if mathA > mathB and englishA > englishB:
    print(1)
else:
    print(0)