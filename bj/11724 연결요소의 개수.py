import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
#정점, 간선
graph=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=graph[b][a]=1

def bfs(x,y):
    queue=deque()
    queue.append(x)
    queue.append(y)
    graph[x][y]=graph[y][x]=0
    while queue:
        a=queue.popleft()

        for i in range(N+1):
            if graph[a][i]==1:
                queue.append(i)
                graph[a][i]=0

cnt=-1
for i in graph:
    if sum(i)==0:
        cnt+=1
for i in range(N+1):
    for j in range(N+1):
        if graph[i][j]==1:
            bfs(i,j)
            cnt+=1
print(cnt)