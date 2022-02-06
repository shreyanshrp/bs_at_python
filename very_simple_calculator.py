#A very Simple calculator in PYTHON , which can calculate using only one operator and two values at a time.
#shreyanshrp (github.com/shreyanshrp)
a= float(input("Enter first value: "))
op= input("Enter operator (from + , - , * , / , ** , // , %): ")
b= float(("Enter second value: "))

if op == "+" :
    print(a + b)
elif op == "-" :
    print(a - b)
elif op == "*" :
    print(a * b)
elif op == "/" :
    print(a / b)
elif op == "**" :
    print(a ** b)
elif op == "%" :
    print(a % b)
elif op == "//" :
    print(a // b)
else :
    print("invalid input, choose operator from given only.")
    exit()
