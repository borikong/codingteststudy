N=int(input())
word=[]
s_word=[]
for i in range(N):
    new=input()
    try :
        word.index(new)
    except:
        word.append(new)
word=list(set(word))

for i in word:
    s_word.append([len(i),i])

word=sorted(s_word)

for i in word:
    print(i[1])