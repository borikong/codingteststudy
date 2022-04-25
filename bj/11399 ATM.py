import sys
N=int(sys.stdin.readline().strip())
p=list(map(int,sys.stdin.readline().strip().split()))
p.sort()
sum=0
for i in range(len(p)):
    for j in range(i+1):
        sum+=p[j]

print(sum)