import sys
# 중복 ok
N, M = map(int, sys.stdin.readline().split())
l = []

def dfs(s):

    if len(l) == M:  ##깊이가 M이면 리스트를 출력하고 return
        print(*l)
        return

    for i in range(s,N+1):
        l.append(i)  ##다음 단계로 가기 전 자기자신을 append
        dfs(i)
        l.pop() ##return할 때 마다 리스트를 비워줌

dfs(1)
