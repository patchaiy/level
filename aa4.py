li,r,n=map(int,input().split())
c=0
for k in range(li,r+1):
   if str(n)in str(k):
       c=c+1
print(c)
