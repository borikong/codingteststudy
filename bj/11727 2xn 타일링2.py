import sys
N=int(sys.stdin.readline().strip())
dp=[0 for i in range(N+4)]

dp[0]=0
dp[1]=1
dp[2]=3
dp[3]=5
dp[4]=11


for i in range(5,N+1):
    dp[i]=dp[i-1]+dp[i-2]*2

print(dp[N]%10007)
