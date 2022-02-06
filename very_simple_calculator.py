#A very Simple calculater in PYTHON , which can calculate using only one operator and two values at a time.
#shreyanshrp (github.com/shreyanshrp)
a= input("Enter first value: ")
op= input("Enter operator (from + , - , * , / , ** , // , %): ")
b= input("Enter second value: ")

a=int(a)
b=int(b)

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
