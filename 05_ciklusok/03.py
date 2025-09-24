
folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n' or valasz == "nem":
        folytatja = False
    elif valasz == "igen":
        print("Csak i és n lehet a válasz")
print('>> Program vége! <<')