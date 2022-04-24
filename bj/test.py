from collections import deque
dx = [0,0,1,-1] #x 좌표 위(고정) 아래(고정) 우 좌
dy = [1,-1,0,0] #y 좌표 아래 위 우(고정) 좌(고정)

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0 #해당 좌표는 0으로 바꿈(벌레가 시작)

    while queue: #큐에 데이터가 없을 때 까지 탐색
        x, y = queue.popleft()
        for i in range(4): #위,아래,좌,우로 탐색(pop한 x,y의 자식노드들, 4개의 자식노드를 가짐)
            nx = x+dx[i] #현재 x좌표에서 위(고정) 아래(고정) 우 좌 로 갈 것인가
            ny = y+dy[i] #현재 y좌표에서 아래 위 우(고정) 좌(고정) 로 갈 것인가

            if nx < 0 or nx >=n or ny < 0 or ny >= m: #맨 끝 부분은 -1이거나 가로,세로 길이보다 크므로 pass
                continue
            if graph[nx][ny] == 1: #bfs로 탐색한 그래프에서 1이 발견된다면
                graph[nx][ny] = 0 #해당 좌표를 0으로 변경
                queue.append((nx, ny)) #해당 좌표의 위,아래,좌,우도 탐색해야 하므로 큐에 추가
        # for i in range(len(graph)):
        #     print(graph[i])

cnt = 0
n, m, k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

for j in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

for i in range(len(graph)):
    print(graph[i])

for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            bfs(graph, a, b)
            cnt += 1
print(cnt)