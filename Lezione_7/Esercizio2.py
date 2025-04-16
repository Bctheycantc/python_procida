# Data la seguente lista di numeri:
# 1. Trova i numeri pari
# 2. Calcola la somma dei numeri dispari
# 3. Trova il numero massimo

numMax = -9999999999
sommaDispari = 0

numeri = [12, 3, 7, 24, 5, 18, 9, 10, 15, 2]
for numero in numeri:
    if numero > numMax:
        numMax = numero
    elif numero % 2 == 0:
        print(numero, "è pari.")
    else:
        sommaDispari += numero
        print(numero)
print("La somma dei numeri dispari è", sommaDispari)
print("Il nummero maggiore è", numMax)