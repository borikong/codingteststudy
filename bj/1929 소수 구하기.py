#에라토스테네스의 체
import sys,math
M,N=map(int,sys.stdin.readline().strip().split())

def isprime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False

    return True
for i in range(M,N+1):
    if isprime(i):
        print(i)
