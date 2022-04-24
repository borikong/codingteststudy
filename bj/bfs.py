from collections import deque
import sys
t=int(sys.stdin.readline())
dx=[0,0,-1,1]
dy=[-1,1,0,0]
def bfs(graph,y,x):
    queue=deque()
    queue.append((y,x))
    graph[y][x]=0

    while queue:
        yy,xx=queue.popleft()
        for i in range(4):
            nx=xx+dx[i]
            ny=yy+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue

            if graph[ny][nx]==1:
                queue.append((ny,nx))
                graph[ny][nx]=0

for i in range(t):
    cnt=0
    m,n,k=map(int,sys.stdin.readline().strip().split())
    graph=[[0]*m for _ in range(n)]

    for i in range(k):
        x,y=map(int,sys.stdin.readline().strip().split())
        graph[y][x]=1

    for y in range(n):
        for x in range(m):
            if graph[y][x]==1:
                bfs(graph,y,x)
                cnt+=1

    print(cnt)
