"""
7️ Hőmérséklet tanács
Kérj be egy hőmérsékletet Celsiusban, és adj tanácsot:
0 alatt: „Nagyon hideg, öltözz melegen!”


0–20: „Hűvös, kabát ajánlott.”


21–30: „Kellemes idő.”


30 felett: „Forróság, igyál sok vizet!”

"""
homerseklet = float(input("Add meg a hőmérsékletet Celsiusban: "))
if homerseklet <= 20:
    print("Hűvös, kabát ajánlott.")
elif homerseklet <= 30:
    print("Kellemes idő.")
elif homerseklet > 30:
    print("Forróság, igyál sok vizet!")