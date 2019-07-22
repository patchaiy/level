def PSUM(ni) :
    sum1 = 0
    while ni :
        sum1 += ni%10
        ni//= 10
    return sum1

def isPrime(ni) :
    if ni==1 : return False
    if ni==2 or ni==3 : return True
    for i in range(2,ni) :
        if ni%i == 0 :
            return False
    return True

a,b = input().split()
a,b = int(a),int(b)
out = 0
for i in range(a,b+1) :
    sum1 = PSUM(i)
    if isPrime(sum1) :
        out += 1
        
print(out)
