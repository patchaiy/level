Ni=int(input())
s=[]
for i in range(2,Ni):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            if i%j!=0 and i+j==Ni:
                b=str(j)+' '+str(i)
                s.append(str(b))
print(s[-1])
