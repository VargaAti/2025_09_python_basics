a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))
operator = input("Add meg a műveleti jelet (+ - * /): ")
#if operator != "+" or operator != "-" or
if operator == "+":
    c = a + b
elif operator == "-":
    c = a - b
elif operator == "/":
    c = a / b
elif operator == "*":
    c = a * b
print("Az eredmény ", c)