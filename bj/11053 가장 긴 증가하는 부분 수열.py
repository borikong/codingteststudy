import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[0 for _ in range(N)]
dp[0]=0
dp[1]=1

for i in range(2, N):
    for j in range(A.index(i)):
        if a[]

# 7
# 1 4 5 2 3 4 5

#1.min 부터 출발해야 한다?? -> 그것도 아님

# print(dp)