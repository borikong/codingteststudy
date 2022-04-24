N=int(input())
for i in range(N):
    b = []
    b_ = []
    b=input()

    for i in b:
        if i=="(" or i=="[":
            b_.append(i)
        elif i==")":
            if len(b_)!=0 and b_[-1]=="(":
                b_.pop()
            else:
                b_.append(i)
        elif i=="]":
            if len(b_) != 0 and b_[-1] == "[":
                b_.pop()
            else:
                b_.append(i)
    if len(b_)==0:
        print("YES")
    else:
        print("NO")