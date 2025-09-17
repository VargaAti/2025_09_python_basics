"""""
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
"""""
PI = 3.14
r = int(input("Add meg a kör átmérőjét cm-ben!"))
kerulet = 2 * r * PI
terulet = PI * r ** 2
print(f"A kör kerülete {kerulet} cm.")
print(f"A kör területe {terulet} cm.")