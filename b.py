Ni=int(input())
q=list(map(int,input().split()))
c=1
for i in q:
    if q.count(i)>c:
        r=i
        c=q.count(i)
print(r)
