import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N)]
for i in range(N):
    a=str(sys.stdin.readline().strip())
    for j in a:
        graph[i].append(int(j))


def bfs(x,y):
    cnt = [[0] * M for _ in range(N)]
    queue=deque()
    queue.append([x,y])
    graph[y][x]=0
    l=[]
    l.append([x,y])
    cnt[y][x]=1
    ax = [0, 0, 1, -1]
    ay = [1, -1, 0, 0]

    while queue:
        a,b=queue.popleft()
        if a==M-1 and b==N-1:
            return cnt

        for i in range(4):
            if b+ay[i]>=0 and b+ay[i]<N and a+ax[i]>=0 and a+ax[i]<M:
                if graph[b+ay[i]][a+ax[i]]==1:
                    queue.append([a+ax[i],b+ay[i]])
                    l.append([a+ax[i],b+ay[i]])
                    graph[b+ay[i]][a+ax[i]]=0
                    cnt[b+ay[i]][a+ax[i]]=cnt[b][a]+1

print(bfs(0,0)[N-1][M-1])