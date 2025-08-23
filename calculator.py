num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter the operation(+, *, -, /): ")

result  = 0

if operator == '+':
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '/':
    if num2 !=0:
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("SECOND NUMBER CANT BE ZERO! ")
else:
    print("INVALID INPUT OPERATOR! ")
