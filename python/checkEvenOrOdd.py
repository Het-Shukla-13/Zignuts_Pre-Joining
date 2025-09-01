def checkParity(num):
    if num%2==0:
        return True
    else:
        return False
    
n=int(input("Enter a number: "))
if checkParity(n):
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")