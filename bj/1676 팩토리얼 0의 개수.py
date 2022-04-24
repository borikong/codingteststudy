N=int(input())

def factorial(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return N*factorial(N-1)

s=list(str(factorial(N)))
num=0
for i in range(len(s)-1,0,-1):
    if s[i]=='0':
        num+=1
    else:
        break
print(num)