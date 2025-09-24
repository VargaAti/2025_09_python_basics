"""
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""
import random
felhasznalo = input("Fej vagy írás?: ")
gep = random.randint(1,2)
fej = 1
iras = 2
print(f"A gép válasza: {gep}")
if felhasznalo == "fej" and gep == fej:
    print("Nyertél!")
elif felhasznalo == "írás" and gep == iras:
    print("Nyertél.")
elif felhasznalo == "fej" and gep == iras:
    print("Vesztettél.")
elif felhasznalo == "írás" and gep == fej:
    print("Vesztettél.")
else:
    print("Hibás adat! az elfogadott adatok: fej, írás")