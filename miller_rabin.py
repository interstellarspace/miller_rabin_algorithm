def getkm(n):
    i = 0
    while(1):
        d = 2**i
        m = (n-1)/d
        if( (m % 2) == 1 ):
            break
        i += 1
    return [i,m]


def miller_rabin(n,a,k,m):
    b = pow(a,m,n)
    
    if (b-1) % n == 0:
        return ("no")
    for i in range(0,k):
        #print(k)
        if (b+1) % n == 0:
            return ("no")
        else:
            b = (b**2) % n
    return("yes")

num = {289,4599,321321,13,777777,7777777}
for n in num:
    yes = 0
    no = 0
    [k,m] = getkm(n)
    #print(str(k)+" "+str(m))
    for a in range(1,n-1):
        s = miller_rabin(n,a,k,m)
        if(s=="yes"):
            yes += 1
        else:
            no += 1
    print("For n = " + str(n) + ": \nStrong false witnesses(" + str(yes) + "), \nNot(" + str(no) + ")\n")