def calculator():
    while True:
        try:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            break
        except ValueError:
            print("Input a valid number.")

    operator = input("Select an operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero."
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    else:
        return "Invalid operator selected."

    return round(result, 3)


print(calculator())
