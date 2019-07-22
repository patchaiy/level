def sumn(n) :
    sum1 = 0
    while n :
        sum1 += n%10
        n //= 10
    return sum1

n = int(input())
if n <= 9:
    print(n)
    sys.exit()
ai = n // 9
b = n % 9
if b :
    out = str(b) + str('9') * ai
else :
    out = str('9') * ai
print(out)
