N,M = map(int,input().split())
def prime(ai):
  flag = 0
  if ai == 2:
    flag = 1
  else:
    for i in range(2,ai+1):
      for j in range(2,i):
        if i%j == 0:
          flag = 0
          break
        else:
          flag = 1
  return flag
ai,b =prime(N),prime(M)
if ai==b==1:
  print('yes')
else:
  print('no')
