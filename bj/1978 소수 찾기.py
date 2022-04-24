import sys
N=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
count=0
isp=False
for i in l:
    if i==0 or i==2:
        count+=1
    else:
        for j in range(2,i):
            if i%j==0 and j!=i:
                isp = False
                break
            else:
                isp=True
    if isp==True:
        count+=1

print(count)