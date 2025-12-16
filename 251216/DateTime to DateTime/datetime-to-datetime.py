a, b, c = map(int, input().split())

# Please write your code here.
START_MIN = (11 * 60) + 11  

end_days_in_min = (a - 11) * 1440
end_time_in_min = (b * 60) + c

end_total_min = end_days_in_min + end_time_in_min

total_minutes = end_total_min - START_MIN

if total_minutes < 0:
    print(-1)
else:
    print(total_minutes)