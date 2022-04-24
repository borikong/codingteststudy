N=int(input())
l=[]
for i in range(N):
    l.append(int(input()))

l.sort()
print(*l,sep="\n")