import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split())
graph=[[0]*(K+1) for _ in range(K+1)]
for i in range(1,K+1):
    minus=i-1
    plus=i+1
    multiply=i*2
    if minus<=17 : graph[i][minus] = 1
    if plus<=17 : graph[i][plus] = 1
    if multiply<=17 : graph[i][multiply] = 1

# for i in range(len(graph)):
#     print(i," : ",graph[i])

def bfs(start):
    queue=deque()
    l=[]
    queue.append(start)
    l.append(start)
    cnt=[0 for i in range(K+1)]
    while queue:
        a=queue.popleft()
        for i in range(K+1):
            if graph[a][i]==1 and (i not in l):
                queue.append(i)
                l.append(i)
                cnt[i]=cnt[a]+1
    return cnt

print(bfs(N)[K])