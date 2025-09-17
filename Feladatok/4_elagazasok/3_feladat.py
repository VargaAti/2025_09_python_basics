"""
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
"""
import random
szemely = int(input("Gondoltam egy számra 1 és 5 között. Találd ki: "))
gep = random.randint(1,5)
# gep = 3
if szemely == gep:
    print("Eltaláltad!")
elif szemely > gep:
    print("A te számod nagyobb, mint az enyém.")
else:
    print("A te számod kisebb, mint az enyém.")