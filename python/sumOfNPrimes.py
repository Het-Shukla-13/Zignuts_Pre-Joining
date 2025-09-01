def sumofNPrimes(n):
    sum=0
    count=0
    if n<=0:
        return 0
    num=2
    while count<n:
        if checkPrime(num):
            sum+=num
            count+=1
        num+=1
    return sum

def checkPrime(num):
    if num<=1:
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True

n=int(input("Enter the no. of primes to sum: "))
print(f"Sum of {n} primes: {sumofNPrimes(n)}")