import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)
l = []
res = []


def dfs(s):

    if len(l) == M:
        res.append([])
        for i in l:
            res[-1].append(numbers[i])
        return
    for i in range(s, N ):
        if len(l)>=1 and i<l[-1]:
            break
        else:
            l.append(i)
            dfs(i)
            l.pop()

dfs(0)
res = sorted(res)
for i in res:
    print(*i, sep=" ")

##반례
##4 4
##9 8 7 1
