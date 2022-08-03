import sys
## 중복 없이
N, M = map(int, sys.stdin.readline().split())
l = []

def dfs(s):
    if len(l) == M:  ##깊이가 M이면 리스트를 출력하고 return
        print(*l)
        return

    for i in range(s,N+1):
        l.append(i)
        dfs(i+1)
        l.pop() ##return할 때 마다 리스트를 비워줌

dfs(1)
