import sys

N=int(sys.stdin.readline())
step=[]
for i in range(N):
    step.append(int(sys.stdin.readline()))

dp=[0 for _ in range(N)]
dp[0]=0
dp[1]=step[1]
dp[2]=step[0]+step[1]

for i in range(3,N):
    dp[i]=max(dp[i-1]+step[i],dp[i-2]+step[i])
    print(i,dp[i],dp[i-1],step[i],dp[i-2],step[i])

print(dp)