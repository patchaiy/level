endi = int(input())
sta = 1
sprime = [True for i in range(endi+1)] 
p = 2
out = []
outlist = []
code = 0
count = 0
while (p * p <= endi): 
    if (sprime[p] == True): 
        for i in range(p * p, endi+1, p): 
            sprime[i] = False
    p += 1
for p in range(sta, endi): 
        if sprime[p] and p!=1: 
            outlist.append(p)
for i in range(len(outlist)):
    for j in range(i,len(outlist)):
        if (outlist[i] + outlist[j]) == endi:
            count += 1
print(count)
