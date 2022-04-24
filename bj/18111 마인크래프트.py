N,M,B = map(int,input().split())
SIZE=N*M
ti=[]
data=[0]*257
min_time=10000000000000000000
max_height=-1
sum_gr=0
it=0
for _ in range(N):
    for i in map(int,input().split()):
        data[i]+=1
        sum_gr+=i

sum_gr+=B
for s in range(0,257,1):
    if sum_gr-(s*SIZE)>=0:
        t = 0
        it=0
        for i in data:
            if i!=0:
                if it-s>0:
                    t+=(it-s)*2*i
                elif it-s<0:
                    t+=(s-it)*1*i
            it += 1

        if t<=min_time and s>max_height:
            min_time=t
            max_height=s
            ti=[min_time,max_height]
    else:
        break

print(ti[0],ti[1])
