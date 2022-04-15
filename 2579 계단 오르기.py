#dynamic programming
import sys
n=int(sys.stdin.readline().strip())
dp=[0 for _ in range(n)]
array=[int(sys.stdin.readline()) for _ in range(n)]
dp[0]=array[0]
if n==1:
    print(array[0])
elif n==2:
    print(array[0]+array[1])
else:
    dp[1]=max(array[0]+array[1],array[1])
    dp[2]=max(array[0]+array[2],array[1]+array[2])
    for i in range(3,n):
        dp[i]=max(dp[i-3]+array[i-1]+array[i],dp[i-2]+array[i])
    print(dp[n-1])

