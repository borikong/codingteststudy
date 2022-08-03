import sys

N,M=map(int, sys.stdin.readline().split())
numbers=list(map(int, sys.stdin.readline().split()))
numbers=sorted(numbers)
l=[]
res=[]

##방법1. numbers를 sort하고 하는 방법
def dfs(s):
    if len(l)==M:
        res.append([])
        for i in l:
            res[-1].append(numbers[i-1])
        print(res)
        return
    for i in range(s,N+1):
        l.append(i)
        dfs(i+1)
        l.pop()

##방법2. for 문 안에서 if로 중복을 제거하는 방법
# def dfs(s):
#     if len(l)==M:
#         res.append([])
#         for i in l:
#             res[-1].append(numbers[i-1])
#         return
#     for i in range(1,N+1):
#         if i not in l: ##if i!=s:
#             l.append(i)
#             dfs(i)
#             l.pop()


dfs(0)
res=sorted(res)

for i in res:
    print(*i,sep=" ")

