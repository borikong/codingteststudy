import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
graph=[[0]*(N+1) for _ in range(N+1)]
t=0
while t<M:
    a,b=map(int,sys.stdin.readline().split())
    if graph[a][b]==1:
        continue
    else:
        graph[a][b]=graph[b][a]=1
        t+=1

def bfs(start):
    l=[]
    cnt=[0 for _ in range(N+1)]
    queue=deque()
    queue.append(start)
    l.append(start)

    while queue:
        temp=queue.popleft()

        for i in range(1,N+1):
            if graph[temp][i]==1 and (i not in l):
                queue.append(i)
                l.append(i)
                ##현재 노드에서 다음노드로 넘어가는것 : 현재 노드의 경로 수+1
                cnt[i]=cnt[temp]+1

    return cnt

cnt=[]
for i in range(N+1):
    cnt.append(sum(bfs(i)))

print(cnt.index(min(cnt[1:N+1])))
