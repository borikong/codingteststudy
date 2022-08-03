import sys
from collections import deque

N=int(sys.stdin.readline())
graph=[[0]*(N+1) for _ in range(N+1)]
res=[]

for i in range(N-1):
    a,b=map(int, sys.stdin.readline().split())
    graph[a][b]=graph[b][a]=1

def bfs(start):
    queue=deque()
    l=[]
    l.append(start)
    queue.append(start)

    while queue:
        v=queue.popleft()

        for i in range(len(graph[v])):
            if graph[v][i]==1 and  i not in l:
                res.append([])
                res[-1].append(i)
                res[-1].append(v)
                queue.append(i)
                l.append(i)
bfs(1)

res=sorted(res)

for i in range(len(res)):
    print(res[i][-1])