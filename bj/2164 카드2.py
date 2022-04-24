import sys,math
N=int(sys.stdin.readline())
L=[i for i in range(1,N+1)]
while len(L)>1:
    print(L)
    L.pop(0)
    temp=L[0]
    L.pop(0)
    L.append(temp)

print(*L)

m=math.log2(N)
if m%1==0:
    m=m-1
else:
    m = math.floor(m)

if N==1:
    print(1)
elif N<6:
    print(2)
else:
    print(int((N-2**m)*2))
