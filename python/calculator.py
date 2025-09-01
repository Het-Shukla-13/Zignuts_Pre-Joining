def calculator(num1, num2, operator):
    match operator:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2
        case '/':
            if num2==0:
                return "Error: Division by zero"
            return num1/num2
        case _:
            return "Error: Invalid operator"
        
while True: 
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    operator=input("Enter operator (+, -, *, /): ")
    result=calculator(num1, num2, operator)
    print(f"Result: {result}")
    ans=input("Do you want to continue? (y/n): ")
    if ans=='n':
        break