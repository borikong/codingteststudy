import sys
def push(stack,x):
    stack.append(x)
    return stack

def pop(stack):
    if len(stack)!=0:
        print(stack.pop())
    else:
        print(-1)
    return stack

def size(stack):
    num=0
    for i in stack:
        if i.isdigit():
            num+=1
    print(num)

def empty(stack):
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top(stack):
    if len(stack)!=0:
        print(stack[-1])
    else:
        print(-1)

N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    c=sys.stdin.readline().split()
    if c[0]=="push":
        stack=push(stack,c[1])
    elif c[0]=="pop":
        stack=pop(stack)
    elif c[0]=="size":
        size(stack)
    elif c[0]=="empty":
        empty(stack)
    elif c[0]=="top":
        top(stack)