import sys
t=int(sys.stdin.readline().strip())
for i in range(t):
    c=int(sys.stdin.readline().strip())
    item=[sys.stdin.readline().strip().split() for _ in range(c)]
    category=[] #카테고리를 저장
    ctcnt=[] #카테고리별 아이템 개수 저장
    for i in range(len(item)):
        if item[i][1] in category:
            ctcnt[category.index(item[i][1])]+=1
        else:
            category.append(item[i][1])
            ctcnt.append(1)
    sum=1
    for i in range(0,len(ctcnt)):
        sum*=(ctcnt[i]+1)
    print(sum-1)
