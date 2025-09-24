"""
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""
import random
random_szam = random.randint(1, 3)
felhasznalo = int(input("Adj meg egy számot 1 és 3 között: "))
if random_szam == felhasznalo:
    print("Eltaláltad")
else:
    print(f"Nem találtad el, a helyes szám {random_szam}")