import sys
target=int(sys.stdin.readline().strip())
bc=int(sys.stdin.readline().strip())
li=list(str(target))
le=len(li)
ans = abs(100 - target)
index = 0
if bc:
    broken = list(map(int, sys.stdin.readline().strip().split()))
else:
    broken=[]

for i in range(1000001):
    index = 0
    for j in str(i):
        if int(j) in broken:
            index=-1
            break
    if index==0:
        ans=min(ans,len(str(i))+abs(target-i))

print(ans)