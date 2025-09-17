"""
4️ Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""
elso = int(input("Add meg az első számot: "))
masodik = int(input("Add meg az második számot: "))
harmadik = int(input("Add meg az harmadik számot: "))
if elso > masodik and elso > harmadik:
    print(f"A legnagyobb szám a(z) {elso}")
elif masodik > elso and masodik > harmadik:
    print(f"A legnagyobb szám a(z) {masodik}")
elif harmadik > elso and harmadik > masodik:
    print(f"A legnagyobb szám a(z) {harmadik}")
else:
    print("Helytelen formátum (Van egyenlő szám)")

"""
Listás megoldás a feladatra
"""
# elso = int(input("Add meg az első számot: "))
# masodik = int(input("Add meg az második számot: "))
# harmadik = int(input("Add meg az harmadik számot: "))
# lista = [elso, masodik, harmadik]
# print(max(lista))