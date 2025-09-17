"""
6️ Egyszerű jelszóellenőrző
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""
jelszo = input("Kérem a jelszót: ")
if jelszo == "titok":
    print("Belépés engedélyezve")
else:
    print("Helytelen jelszó")