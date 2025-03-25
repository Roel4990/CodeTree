secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class meetCode:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

meeting1 = meetCode(secret_code, meeting_point, time)

print(f"secret code : {meeting1.secret_code}")
print(f"meeting point : {meeting1.meeting_point}")
print(f"time : {meeting1.time}")