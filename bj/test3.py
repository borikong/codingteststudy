li=[1,1,2,3,5,8]
li2=[]

for a in range(6):
    li2.append(li.pop())
li=li2
print(li)
li2=[]
for a in range(6):
    li2.append(li.pop())

li=li2
print(li)

li.pop(0)
print(li)