import sys
from collections import deque
#부모노드가 있으면 부모부터->자신->자식

n,v,s=map(int,sys.stdin.readline().strip().split())
#노드 개수, 간선 개수, 첫 시작 노드
node=[[0]*(n+1) for _ in range(n+1)] ##0~n개 노드 (리스트의 특성 때문에 1을 더해 줌)

def bfs(s):
    l=[]
    queue=deque()
    queue.append(s)
    l.append(s)

    while queue:
        v=queue.popleft()
        print(v,end=" ")

        for i in range(len(node[s])):
            if node[v][i]==1 and (i not in l):
                l.append(i)
                queue.append(i)

def dfs(s,l):
    l.append(s)
    print(s,end=" ")
    for i in range(len(node[s])):
        if node[s][i]==1 and (i not in l):
            dfs(i,l)

for i in range(v):
    a,b=map(int,sys.stdin.readline().strip().split())
    node[a][b]=node[b][a]=1

print(node)
l=[]
dfs(s,l)
print()
bfs(s)