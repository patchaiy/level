Si,A=list(map(str,input().split()))
p=[]
for i in Si:
    for j in A:
        if i==j:
            p.append(i)
print("".join(p))
