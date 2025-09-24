"""
4. Feladat
Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
"""
szoveg = input("Adj meg egy szöveget: ")
gep = 0
szam = int(input("Hányszor szeretnéd megismételni? "))
while gep != szam:
    print(szoveg)
    gep = gep + 1