import sys

# def fibonacci(s,p):
#     if p

n=int(sys.stdin.readline())
s=[int(sys.stdin.readline().strip()) for i in range(n)]
dp=[0 for i in range(n+1)]
p=[[0] for i in range(n+1)]

print(s)
dp[1]=20
dp[2]=30
p[1]=[0,1]
p[2]=[0,1,2]
for i in range(3,n+1):
    if p[i-1][-1]==n-1 and p[i-1][-2]==n-2:
        dp[i]=max(dp[i-1],p[i-2]+s[i-1]) ##s[i]
        if dp[i]==dp[i-1]:
            p[i]=p[i-1]
        else:
            p[i]=[0,i-2,i]
    if p[i-1][-1]==n-2:
        dp[i]=dp[i-2]+dp[i]
    # print(dp[i-1]+s[i],dp[i-2]+s[i-1])
    print(dp)

print(dp[n])