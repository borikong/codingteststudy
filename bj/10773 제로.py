import sys
N=int(sys.stdin.readline())
num=[]
for i in range(N):
    a=int(input())
    if a!=0:
        num.append(a)
    elif a==0:
        num.pop()

print(sum(num))