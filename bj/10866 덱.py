import sys
def push_front(deque,x):
    temp=[]
    temp.append(x)
    return temp+deque

def push_back(deque,x):
    deque.append(x)
    return deque

def pop_front(deque):
    if len(deque)==0:
        print(-1)
    else:
        print(deque.pop(0))
        return deque

def pop_back(deque):
    if len(deque)==0:
        print(-1)
    else:
        print(deque.pop())
        return deque
def size(deque):
    print(len(deque))

def empty(deque):
    if len(deque)==0:
        print(1)
    else:
        print(0)

def front(deque):
    if len(deque)==0:
        print(-1)
    else:
        print(deque[0])

def back(deque):
    if len(deque)==0:
        print(-1)
    else:
        print(deque[-1])

N=int(sys.stdin.readline())
deque=[]
for i in range(N):
    c=sys.stdin.readline().split()

    if c[0]=="push_front":
        deque=push_front(deque,c[1])
    elif c[0]=="push_back":
        deque=push_back(deque,c[1])
    elif c[0]=="pop_front":
        pop_front(deque)
    elif c[0]=="pop_back":
        pop_back(deque)
    elif c[0]=="size":
        size(deque)
    elif c[0]=="empty":
        empty(deque)
    elif c[0]=="front":
        front(deque)
    elif c[0]=="back":
        back(deque)