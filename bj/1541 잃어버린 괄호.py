import sys
md=sys.stdin.readline().strip().split("-")

sum=0
for i in md[0].split("+"):
    sum+=int(i)

for i in md[1:]:
    for j in i.split("+"):
        sum-=int(j)

print(sum)

