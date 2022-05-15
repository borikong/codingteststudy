import sys
from collections import deque
N=int(sys.stdin.readline())
graph=[[] for _ in range(N)]
for i in range(N):
    a=str(sys.stdin.readline().strip())
    for j in a:
        graph[i].append(int(j))

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    graph[y][x]=0
    xp=[0,0,1,-1]
    yp=[1,-1,0,0]
    cnt=1
    while queue:
        xx,yy=queue.popleft()

        for i in range(4):
            xxx=xx+xp[i]
            yyy=yy+yp[i]
            if xxx>=0 and xxx<N and yyy>=0 and yyy<N:
                if graph[yyy][xxx]==1:
                    graph[yyy][xxx] =0
                    queue.append([xxx,yyy])
                    cnt+=1
    return cnt

cnt=[]
all=0
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            cnt.append(bfs(j,i))
            all+=1
cnt.sort()
print(all)
print(*cnt,sep="\n")