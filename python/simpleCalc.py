def calculate(a: float, b: float, operand: str)-> float:
    match operand:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                raise ValueError("Division by zero is not allowed.")    
            return a / b
        case '//':
            if b == 0:
                raise ValueError("Division by zero is not allowed.")
            return a // b
        case '%':
            if b == 0:
                raise ValueError("Division by zero is not allowed.")
            return a % b
        case '**':
            return a ** b
        case _:
            raise ValueError(f"Unsupported operand: {operand}. Use one of +, -, *, /, //, %, **.")
        
def main():
    print("Simple Calculator")
    while True:
        try:
            expr=input("Enter expression (or 'exit' to quit) (Expression Format: a operand b): ")
            if expr.lower()=='exit':
                print("Exiting the calculator. Goodbye!")
                break
            a, operand, b = expr.split()
            a=float(a)
            b=float(b)
            result=calculate(a, b, operand)
            print(f"Result: {a} {operand} {b} = {result}")
        except ValueError as err:
            print(f"Error: {err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

main()