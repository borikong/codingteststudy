import sys
N,M=map(int,sys.stdin.readline().split())
h=set([sys.stdin.readline().strip() for i in range(N)])
s=set([sys.stdin.readline().strip() for i in range(M)])
hs=[]
q=h.intersection(s)
for i in q:
    hs.append(i)
hs.sort()
print(len(hs))
print(*hs,sep="\n")