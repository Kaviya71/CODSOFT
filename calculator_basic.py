def calculator():
    print("===== Simple Calculator =====")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Choose operation: + | - | * | / ")
    op = input("Enter operation: ")
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2

    else:
        print("Invalid operation!")
        return
    
    print(f"Result: {num1} {op} {num2} = {result}")

calculator()
