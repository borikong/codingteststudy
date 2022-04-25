#dynamic programming
import sys
t=int(sys.stdin.readline().strip())
for i in range(t):
    num=int(sys.stdin.readline().strip())
    p=[0 for _ in range(num+6)]
    p[0]=0
    p[1]=1
    p[2]=1
    p[3]=1
    p[4]=2
    p[5]=2

    for i in range(6,num+1):
        p[i]=p[i-1]+p[i-5]

    print(p[num])