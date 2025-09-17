"""
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""
allapot = input("Milyen napod van ma? (Igen vagy nem): ")
if allapot == "Igen":
    print("Szuper, maradjon is így!")
elif allapot == "Nem":
    print("Fel a fejjel!")
