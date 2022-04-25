import sys
N=int(sys.stdin.readline().strip())

for i in range(N):
    num=int(sys.stdin.readline().strip())
    dp=[0 for i in range(num+3)]
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for i in range(4,num+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

    print(dp[num])
