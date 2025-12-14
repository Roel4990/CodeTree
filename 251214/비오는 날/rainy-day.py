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
all_data = list(zip(date, day, weather))
rain_records = [record for record in all_data if record[2] == 'Rain']
earliest_rain_record = min(rain_records)

class Info:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

info1 = Info(earliest_rain_record[0], earliest_rain_record[1], earliest_rain_record[2])

print(info1.date, info1.day, info1.weather)