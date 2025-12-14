n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Info:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

min_rain_index = weather.index("Rain")

info1 = Info(date[min_rain_index], day[min_rain_index], weather[min_rain_index])

print(info1.date, info1.day, info1.weather)