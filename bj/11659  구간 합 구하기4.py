import sys
N,M=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
numarr=[0]
a=0
for i in num:
    a+=i
    numarr.append(a)
for i in range(M):
    i,j=map(int,sys.stdin.readline().split())
    print(numarr[j]-numarr[i-1])

