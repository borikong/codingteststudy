import sys
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
s=str(sys.stdin.readline())
ss="IOI"
for i in range(N-1):
        ss+="OI"

new=""
cnt=0
for i in s:
    new+=i
    if new.count(ss)>=1:
        new="I"
        cnt+=1

print(ss)
print(new)
print(cnt)