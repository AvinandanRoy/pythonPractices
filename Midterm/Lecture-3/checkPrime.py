
# checking Prime number :---->

def isPrime(nmbr):
    if nmbr <= 1 :
        return False
    for i in range(2,int(nmbr**0.5)+1):
        if nmbr % i == 0 :
            return False
    
    return True 

num= int(input("Enter Your Nmbr : "))

if isPrime(num ):
    print(f'{num} is Prime number..')
else:
    print(f'{num} is not Prime number..')