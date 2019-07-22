Ni=input()
li=[]
l=[]
k=[]
a=[]
o=[]
for i in range(0,len(Ni)+1):
    for j in range(0,len(Ni)+1):
        li.append(Ni[i:j])
for i in li:
    if i!='':
        l.append(i)
for i in l:
    r="".join(reversed(i))
    a.append(r)
for i in l:
    for j in a:
        if i==j:
            k.append(i)
for i in k:
    o.append(len(i))
print(max(o))
