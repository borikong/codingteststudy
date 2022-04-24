import sys
N=int(sys.stdin.readline().strip())

for i in range(N):
    num=int(sys.stdin.readline().strip())
    dp=[0 for i in range(num+1)]
    dp[0]=0
    dp[1]=1 #1
    dp[2]=2 ##dp[1]+dp[1] 1+1, 2
    dp[3]=4 #1+1+1,1+2,2+1,3
    for i in range(4,num+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
    print(dp)

# 1+1+1+1
# 1+1+2
# 1+2+1
# 1+3
#
# 1+1+1+1
# 2+2
#
# 1+1+1+1
# 1+2+1
# 2+1+1
# 3+1