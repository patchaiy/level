Ni=int(input())
a=0
for i in range(2,Ni+1):
    fact=0
    rem=i%10
    if(rem==3):
        for j in range(1,i+1):
            if(i%j==0):
                fact+=1
        if(fact==2):
            a=a+i
print(a)
