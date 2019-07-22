Se=input()
ll=[]
for i in range(0,len(Se)):
    for j in range(i+2,len(Se)+1):
        aa=Se[i:j]
        if aa==aa[::-1]:
            ll.append(aa)
ll.sort()
for i in range(0,len(ll)):
    print(ll[i])
