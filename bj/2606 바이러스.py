import sys
from collections import deque
c=int(sys.stdin.readline().strip())
p=int(sys.stdin.readline().strip())
com=[[0]*(c+1) for _ in range(c+1)]

def bfs(start):
    l=[]
    l.append(start)
    queue=deque()
    queue.append(start)

    while queue:
        v=queue.popleft()

        for i in range(len(com[v])):
            if com[v][i]==1 and (i not in l):
                l.append(i)
                queue.append(i)

    return l

for i in range(p):
    a,b=map(int,sys.stdin.readline().strip().split())
    com[a][b]=com[b][a]=1
cnt=len(bfs(1))-1

print(cnt)