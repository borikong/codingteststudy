import sys
from collections import deque

#bfs 이용해서 풀이
##상자라 똑같은 matrix 만들어서 거기에 횟수를 넣어주기
##1을 채워주는 것이 아님
##모든 경우의 수를 탐색하고 max를 이용해서 찾음
M, N = map(int, sys.stdin.readline().split())
box = [[0] * (M) for _ in range(N)]
queue=deque()

for i in range(N):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if line[j]==1:
            queue.append([j,i])
        box[i][j]=line[j]

# print(*box, sep="\n")

vx = (0, 0, -1, 1)
vy = (-1, 1, 0, 0)


def bfs():

    while queue:
        x, y = queue.popleft()
        ##위, 아래, 왼, 오 x(0,0,-1,1) y(-1,1,0,0)
        for j in range(4):
            xx = x + vx[j]
            yy = y + vy[j]
            if 0<= yy <N and 0 <= xx < M :
                if box[yy][xx] == 0:
                    box[yy][xx] = box[y][x]+1
                    queue.append([xx,yy])


bfs()
cnt=0
flag=False
for i in range(N):
    for j in range(M):
        if box[i][j]==0:
            cnt=0
            flag=True
            break
        else:
            cnt=max(cnt,box[i][j])
    if flag:
        break

# print("==============")
# print(*box, sep="\n")

print(cnt-1)
