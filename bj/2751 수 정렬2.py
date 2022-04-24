import sys
N=int(input())
p=[[i,0] for i in range(10001)]
for i in range(N):
    number=int(sys.stdin.readline())
    p[number][0] = number
    p[number][1]+=1

num=0
for i in range(len(p)+1):
    if num==N:
        break
    if p[i][1]!=0:
        for j in range(p[i][1]):
            print(p[i][0])
        num+=p[i][1]
