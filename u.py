Ni=int(input())
l=list(map(str,input().split()))
k=[]
for i in l:
    k.append(i.lower())
k.sort()
for i in k:
    print(i)
