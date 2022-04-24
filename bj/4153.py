while True:
    a=list(map(int,input().split()))
    if a[0]==0 and a[1]==0 and a[2]==0:
        break
    n=max(a)
    a.pop(a.index(max(a)))
    if n**2==a[0]**2+a[1]**2:
        print("right")
    else:
        print("wrong")