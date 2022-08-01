import sys
N,M=map(int, sys.stdin.readline().split())
graph=[[0]*N for _ in range(N)]
l=[]
for i in range(N):
    for j in range(N):
        if j>i :
            graph[i][j]=1

print(*graph, sep="\n")

def dfs(s,cnt):
    l.append(s)
    print(s)
    for i in range(N):
        if graph[s][i]==1:
            dfs(i)
    print(l)
dfs(0,0)

for i in l[1:]:
    for j in range(M):
        print(i+1, end="")
    print()


