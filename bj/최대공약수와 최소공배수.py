#유클리드 호제법

M,N=map(int,input().split())

def GCD(M,N):
    if N==0:
        return M
    return GCD(N,M%N)
print(GCD(M,N))
print(int((M*N)/GCD(M,N)))
