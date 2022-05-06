import sys
N=int(sys.stdin.readline())
time=[]
for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    time.append([a,b])
time.sort(key=lambda x:(x[1],x[0]))
cnt=1
end=time[0][1]
for i in range(len(time)-1):
    if time[i+1][0]>=end:
        cnt+=1
        end=time[i+1][1]
print(cnt)