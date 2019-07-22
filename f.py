Ni=int(input())
if Ni==1:
    print("YES")
elif Ni%2!=0:
    print("NO")
else:
    while Ni%2==0:
        Ni=Ni//2
    if Ni==1:
        print("YES")
    else:
        print("NO")
