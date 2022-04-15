import sys
from collections import deque

N,M=map(int,sys.stdin.readline().strip().split())
graph=[[0]*(N+1) for _ in range(N+1)]
def dfs(start,l):
    l.append(start)
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and (i not in l):
            graph[start][i] = graph[i][start] = 0
            l.append(i)
            dfs(i,l)

def bfs(start,x):
    l=[]
    queue=deque()
    l.append(start)
    queue.append(start)

    while queue:
        v=queue.popleft()

        for i in range(len(graph[v])):
            if graph[v][i]==1 and (i not in l):
                graph[v][i]=graph[i][v]=0
                l.append(i)
                queue.append(i)

    for i in range(len(graph)):
        print(graph[i])
    print()


for i in range(M):
    a,b=map(int,sys.stdin.readline().strip().split())
    graph[a][b]=graph[b][a]=1

cnt=0
# for i in range(len(graph)):
#     print(graph[i])
# print()
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            dfs(i,[])
            cnt+=1

print(cnt-1)