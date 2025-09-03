print("1. összeadás 2. kivonás")
operator = input()
print("Add meg az első számot")
a = int(input())
print("Add meg a második számot")
b = int(input())
if operator == "1":
    c = a + b
else:
    c = a - b
print(c)