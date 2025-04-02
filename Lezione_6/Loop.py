# Con i loop ho la possibilita' di ripetere un blocco di codici

# LOOP INDEFINITI - Sono dei loop che ciclano all'infinito

# while true:
#     print("Ciao")

# While con variabile flag o counter esterno
numStop = 0

while numStop < 10:
    numStop += 1
    print("Adesso il numero vale, ", numStop)

# Esempio pratico

numMaggiore = -9999999999

numero = int(input("Inserisci un numero oppure digita -1 per fermare il loop \n"))

while numero != -1:
    if numero > numMaggiore:
        numMaggiore = numero
    numero = int(input("Inserisci un numero oppure digita -1 per fermare il loop \n"))

print("Il numero piu' grande e' ", numMaggiore)