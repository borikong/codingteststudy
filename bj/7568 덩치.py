N=int(input())
p=[]

rank=[]
for i in range(N):
    a=list(map(int,input().split()))
    a.append(i)
    p.append(a)
    rank.append(-1)

num=1
acc=0
for i in range(0,len(p)):
    for j in range(0,len(p)):
        if p[i][0]<p[j][0] and p[i][1]<p[j][1]:
            num+=1

    rank[i]=num
    num=1

print(*rank)

