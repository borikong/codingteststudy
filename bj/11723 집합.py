import sys

def add(s,x):
    if x not in s:
        s.add(x)
    return s

def remove(s,x):
    try:
        s.remove(x)
    except:
        pass
    return s

def check(s,x):
    if x in s:
        print(1)
    else:
        print(0)

def toggle(s,x):
    if x in s:
        s.remove(x)
    elif x not in s:
        s.add(x)
    return s

def all():
    s={i for i in range(1,21)}
    return s

def empty(s):
    s.clear()
    return s

N=int(sys.stdin.readline())
s=set([])

for i in range(N):

    a=sys.stdin.readline().split()

    if a[0]=="add":
        s=add(s,int(a[1]))
    elif a[0]=="remove":
        s=remove(s,int(a[1]))
    elif a[0] == "check":
        check(s, int(a[1]))
    elif a[0]=="toggle":
        s=toggle(s,int(a[1]))
    elif a[0]=="all":
        s=all()
    elif a[0]=="empty":
        s=set([])