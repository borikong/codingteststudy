import sys
from collections import deque

#위, 아래, 왼쪽, 오른쪽, 앞, 뒤
##M,N 상자크기 H 높이
M,N,H=map(int, sys.stdin.readline().split())
box=[[[0]*(M) for _ in range(N)] for _ in range(H)]
for h in range(H):
    for j in range(N):
        line=list(map(int, sys.stdin.readline().split()))
        box[h][j]=line

print(*box[0], sep="\n")

#1 익었다 0 익지않았다 -1 없다
vx=(0,0,-1,1)
vy=(-1,1,0,0)

def dfs(x,y,l):
    l.append([x,y])

    for j in range(4):
        xx = x + vx[j]
        yy = y + vy[j]

        if xx >= 0 and xx < M and yy >= 0 and yy < N and ([xx, yy] not in l): #박스 상자 범위 내에 있고 이미 탐색한 노드가 아니라면
            if box[yy][xx]==0:
                box[yy][xx]=1
                l.append([xx,yy])
            e





dfs(3,1,box[0])

print("==============")
print(*box[0], sep="\n")

