import sys
from collections import deque

N,M,V=map(int, sys.stdin.readline().split())
node=[[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b=map(int, sys.stdin.readline().split()) ##y, x
    node[a][b]=node[b][a]=1

def bfs(start):
    l=[]
    queue=deque()
    queue.append(start)
    l.append(start)

    while queue:
        v=queue.popleft()

        for i in range(len(node[v])):
            if node[v][i]==1 and i not in l:
                queue.append(i)
                l.append(i)

    return l


def dfs(start,l):
    l.append(start)

    for i in range(len(node[start])):
        if node[start][i]==1 and i not in l:
            dfs(i,l)

    return l


print(*dfs(V,[]), sep=" ")
print(*bfs(V),sep=" ")