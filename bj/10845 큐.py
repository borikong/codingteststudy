import sys
def push(queue,x):
    queue.append(x)
    return queue

def pop(queue):
    if len(queue)!=0:
        a=queue[0]
        queue.remove(a)
        print(a)
    else:
        print(-1)
    return queue

def size(queue):
    num=0
    for i in queue:
        if i.isdigit():
            num+=1
    print(num)

def empty(queue):
    if len(queue)==0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue)!=0:
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if len(queue)!=0:
        print(queue[-1])
    else:
        print(-1)

N=int(sys.stdin.readline())
queue=[]
for i in range(N):
    c=sys.stdin.readline().split()
    if c[0]=="push":
        queue=push(queue,c[1])
    elif c[0]=="pop":
        queue=pop(queue)
    elif c[0]=="size":
        size(queue)
    elif c[0]=="empty":
        empty(queue)
    elif c[0]=="front":
        front(queue)
    elif c[0]=="back":
        back(queue)