L=int(input())
r=31
M=1234567891
s=0
c=list(input())
a=[]
for i in c:
    a.append(ord(i)-96)

for i in range(L):
    s=s+a[i]*r**i

print(s%M)
