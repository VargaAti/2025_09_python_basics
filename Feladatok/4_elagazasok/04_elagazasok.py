"""
Pozitív-negatív számok
"""
# szam = int(input("Adj meg egy egész számot: "))
# if szam < 0:
#     print("Negatív")
# elif szam == 0:
#     print("Nulla")
# else:
#     print("Pozitív")

"""
Páros-páratlán számok
"""
szam = int(input("Adj meg egy egész számot: "))
if szam % 2 == 0 and szam != 0:
    print("Páros")
elif szam == 0:
    print("Nulla")
else:
    print("Páratlan")