import sys
N=int(sys.stdin.readline())
c1=list(map(int,sys.stdin.readline().split()))
l=[0 for i in range(20000001)]
for i in c1:
    a=i+10000000
    l[a]+=1
n=int(sys.stdin.readline())
c2=list(map(int,sys.stdin.readline().split()))

for i in c2:
    a=i+10000000
    print(l[a],end=" ")