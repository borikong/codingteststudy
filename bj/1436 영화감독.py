N=int(input())
dnum=666
dlist=[]
while True:
    test = str(dnum)
    s = test.replace("666", "")
    if len(s)<len(test):
        dlist.append(dnum)
    if len(dlist) == N:
        break
    else:
        dnum += 1
print(dlist[-1])