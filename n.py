Ni=int(input())
a=[]
c=0
for i in range(2,Ni):
    for j in range(2,i+1):
        if i%j==0:
            break
    if j==i:
        a.append(i)
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if a[i]+a[j]+a[k]==Ni:
                print(str(a[i])+" "+str(a[j])+" "+str(a[k]))
                c=1
                break
        if c==1:
            break
    if c==1:
        break
