Ai,B=input().split()
temp=""
def string(n):
   x=""
   for i in range(1,n+1):
      x+=str(i)
   return x
if len(B)>len(Ai):
   Ai+=string(len(B)-len(Ai))
elif len(Ai)>len(B):
   B+=string(len(Ai)-len(B))
for i in range(len(Ai)):
   temp+=(Ai[i]+B[i])
print(temp)
