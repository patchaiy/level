ai=int(input())
SUM=0
b=str(ai)
s=[]
for i in range(0,len(b)):
    SUM=SUM+int(b[i])
    s.append(SUM)
print(sum(s))
