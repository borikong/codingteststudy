import sys
def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n=int(sys.stdin.readline())
l=[0 for i in range(42)]

for i in range(n):
    a=int(sys.stdin.readline())

    for j in range(a+2):
        if j==0 or j==1 or j==2:
            l[j]=fibonacci(j)
        elif l[j]==0:
            l[j]=+l[j-1]+l[j-2]

    one=l[a]
    zero=l[a+1]-one
    print(zero,one)
    # #0의 개수 fibonacci(a+1)-fibonacci(a)

