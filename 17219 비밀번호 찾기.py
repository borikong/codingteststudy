import sys
N,M=map(int,sys.stdin.readline().split())
d=dict()
for i in range(N):
    a=sys.stdin.readline().strip().split()
    d[a[0]]=a[1]

for i in range(M):
    a=sys.stdin.readline().strip()
    print(d[a])