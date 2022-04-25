import sys
N,K=map(int,sys.stdin.readline().strip().split())
coin=[int(sys.stdin.readline().strip()) for _ in range(N)]
cnt=[0 for _ in range(N)]
left=K
for i in range(N-1,-1,-1):
    cnt[i]=left//coin[i]
    left=left%coin[i]

    if left==0:
        break
print(sum(cnt))
