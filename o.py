Ni=int(input())
s=0
while(Ni!=0):
  i=Ni%10
  s=s+i**2
  Ni=Ni//10
print(s)
