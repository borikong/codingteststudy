N=int(input())
p=[]
for i in range(N):
    a=input().split()
    p.append([int(a[0]),i,a[1]])

p.sort()
for i in p:
    print(i[0],i[2])