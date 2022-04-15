from collections import deque
import sys

n,v,start=map(int,sys.stdin.readline().strip().split())
graph=[[0]*(n+1) for _ in range(n+1)]
def bfs(start):
    l=[]
    l.append(start)
    queue=deque()
    queue.append(start)

    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in range(len(graph[v])):
            if graph[v][i]==1 and (i not in l):
                l.append(i)
                queue.append(i)

def dfs(start,l):
    l.append(start)
    print(start,end=" ")
    for i in range(len(graph[start])):
        if graph[start][i]==1 and (i not in l):
            dfs(i,l)

for i in range(v):
    a,b=map(int,sys.stdin.readline().strip().split())
    graph[a][b]=graph[b][a]=1

l=[]
dfs(start,l)
print()
bfs(start)