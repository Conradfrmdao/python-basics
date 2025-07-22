operator=input("Enter an operator (+, -, *, /): ")
numb1=float(input("Enter first number: "))
numb2=float(input("Enter second number: "))
if operator == '+':
    result = numb1 + numb2
    print("The result is:", result)
elif operator== '-':
    result = numb1 - numb2
    print("The result is:", result)
elif operator =='*':
    result = numb1 * numb2
    print("The result is:", result)
elif operator == '/':
    if numb2 != 0:
        result = numb1 / numb2
        print("The result is:", result)
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator"