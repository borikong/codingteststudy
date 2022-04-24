n=int(input())
l=list(map(int,str(n)))
c=[]
m=n-9*(len(l)-1)-l[0]
for i in range(m,n):
    ml=list(map(int,str(i)))
    s=0
    for j in ml:
        s=s+j
    if i+s==n:
        c.append(i)

if len(c)==0:
    print(0)
else:
    print(min(c))