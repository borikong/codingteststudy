import sys
n=int(sys.stdin.readline())
p=[]
for i in range(n):
    li=list(map(int,input().split()))
    p.append([li[1],li[0]])

p.sort()
for i in range(n):
    print(p[i][1],p[i][0])