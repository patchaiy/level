from itertools import permutations
iN=input()
k=permutations(Ni)
l=[]
m=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==Ni:
  print(Ni)
elif Ni==a[::-1]:
  print("-1")
else:
    Ni=tuple(Ni)
    for i in k:
        l.append(i)
    for i in l:
        if i>Ni:
            m=i
            break

    for i in l:
        if i>Ni and i<m:
            m=i

    if m==-1:
        print("-1")
    else:
        for i in m:
            print(i,end="")
