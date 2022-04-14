import sys
N,Q=map(int,sys.stdin.readline().split())
po=[sys.stdin.readline().strip() for i in range(N)]
a=[]
for i in range(Q):
    q=sys.stdin.readline().strip()
    try:
        q=int(q)
        a.append(po[q-1])
    except:
        a.append(po.index(q)+1)

print(*a,sep='\n')