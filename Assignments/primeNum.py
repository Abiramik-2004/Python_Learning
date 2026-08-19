def primeNum(n):
    isprime=True
    if(n<2):
        isprime=False

    else :
        
        for i in range(2,n):
            if(n%i==0):
                isprime=False
                break
    if (isprime):
        print("Prime Number")
    else:
        print("Not a prime number")
primeNum(5)
primeNum(52)
                
