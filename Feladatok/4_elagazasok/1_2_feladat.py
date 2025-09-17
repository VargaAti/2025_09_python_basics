"""
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
"""
allapot = input("Milyen napod van ma? (Igen vagy nem): ")
if allapot == "Igen":
    print("Szuper, maradjon is így!")
elif allapot == "Nem":
    print("Fel a fejjel!")
else:
    print("Sajnos nem érte a válaszodat!")