Ni=input()
temp=""
f=0
for i in range(len(Ni)):
  if Ni[i]==" ":
    temp+=Ni[i]
  elif f==0:
    temp+=Ni[i].upper()
    f=1
  elif f==1:
    temp+=Ni[i]
    f=0
print(temp)
