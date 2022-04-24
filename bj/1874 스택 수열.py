import sys
n=int(sys.stdin.readline().strip())
li=[int(sys.stdin.readline().strip()) for i in range(n)]
stack=[]
ans=[]
i=1

def push(stack,i):
    stack.append(i)
    ans.append("+")
    return stack

def pop(stack):
    stack.pop()
    ans.append("-")
    return stack

while len(li)!=0:
    if len(stack)==0:
        stack=push(stack,i)
        i+=1
    if stack[-1]==li[0]:
        stack=pop(stack)
        li.remove(li[0])
    elif stack[-1]<=li[0]:
        stack=push(stack, i)
        i += 1
    else:
        ans.clear()
        ans.append("NO")
        break

print(*ans,sep="\n")
