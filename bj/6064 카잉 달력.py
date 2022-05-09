import sys
T=int(sys.stdin.readline())

def gcd(M,N):
    if N==0:
        return M
    return gcd(N,M%N)

for i in range(T):
    M,N,x,y=map(int,sys.stdin.readline().split())
    ans=-1
    g=int(M*N/gcd(max(M,N),min(M,N)))
    for year in range(g):
        if year%M==x and year%N==y:
            ans=year
            break
    print(ans)


# M=10
# N=12
#
# <1:1>
# <2:2>
# <3:3>
# <4:4>
# <5:5>
# <6:6>
# <7:7>
# <8:8>
# <9:9>
# <10:10>
# <1:11>
