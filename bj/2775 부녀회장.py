T=int(input())
tr=[]
for i in range(T):
    k=int(input())
    n=int(input())
    people=[[0 for col in range(n)] for row in range(k+1)]

    for i in range(k+1): #i=층
        if i == 0:
            for j in range(n):
                people[0][j]=j+1
        else:
            for j in range(n):
                people[i][j]=sum(people[i-1][:j+1])
    print(people[k][n-1])
    tr.append(people[k][n-1])

for i in tr:
    print(i)

