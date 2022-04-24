import math
A,B,V=map(int,input().split())

day=math.ceil((V-A)/(A-B)) #마지막일자 낮까지 기어오른 데이
left=V-(A*day-B*(day-1))
if left<=0:
    print(day)
elif left>0:
    print(day+1)
