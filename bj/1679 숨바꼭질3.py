import sys,math
N,K=map(int,sys.stdin.readline().split())
cnt=0
num=N
ans=0
while num!=K:
    print(num,cnt)
    if num>K:
        ans=cnt+min(abs(K-num/2),abs(K-num))
        break
    else:
        num*=2
        cnt+=1

print(ans)