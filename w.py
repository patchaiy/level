si=input()
n=1
if len(si)==1:
    print("yes")
else:
    for j in si:
        if si.count(j)==len(si):
            print("no")
            n=0
            break
    if n==1:
        print("yes")
