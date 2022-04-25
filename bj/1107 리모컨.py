import sys
N=int(sys.stdin.readline().strip())
bc=int(sys.stdin.readline().strip())
li=list(str(N))
le=len(li)
if bc==0:
    print(len(li))
else:
    ch = list(map(int, sys.stdin.readline().strip().split()))
    mincnt=abs(100-N)
    index=0

    for i in range(1000001):
        index = 0
        for j in str(i):
            if int(j) in ch:
                index=-1
                break
        if index==0:
            mincnt=min(mincnt,len(str(i))+abs(N-i))

    print(mincnt)