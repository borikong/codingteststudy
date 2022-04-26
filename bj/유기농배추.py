import sys
from collections import deque

t=int(sys.stdin.readline().strip())
M, N, K =0,0,0

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    farm[y][x]=0

    while queue:
        xx,yy=queue.popleft()
        point=[[xx,yy-1],[xx,yy+1],[xx+1,yy],[xx-1,yy]]

        for i in point:
            px,py=i[0],i[1]
            if py < N and py >= 0 and px < M and px >= 0:
                if farm[py][px] == 1:
                    queue.append([px,py])
                    farm[py][px] = 0

for c in range(t):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    farm = [[0] * M for _ in range(N)]
    for i in range(K):
        x,y=map(int,sys.stdin.readline().strip().split())
        farm[y][x]=1

    cnt=0

    for i in range(N):
        for j in range(M):
            if farm[i][j]==1:
                cnt+=1
                bfs(j,i)

    print(cnt)

