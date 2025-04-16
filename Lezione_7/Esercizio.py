# Scrivi un programma che stampa tutti i numeri da 1 a 100
# Per i multipli di 3 stampa "BOOM"
# Per i multipli di 5 stampa "ZOOM"
# Per i multipli di 3 e 5 stampa "BAZINGA"

for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("BAZINGA")
    elif numero % 3 == 0:
        print("BOOM")
    elif numero % 5 == 0:
        print("ZOOM")
    else:
        print(numero)