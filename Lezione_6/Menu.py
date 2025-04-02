# Esempio loop indefinito

scelta = ""

while scelta != "q":
    print("-----MENU-----")
    print("a) Gioca")
    print("b) Calcola")
    print("c) Saluta")
    print("q) Esci")
    print("--------------")
    scelta = str(input("Scegli una voce del menu: \n"))

    if scelta == "a":
        print("Hai scelto di giocare")
    elif scelta == "b":
        print("Hai scelto di calcolare qualcosa")
    elif scelta == "c":
        print("Hai scelto di salutare qualcuno")
    elif scelta == "q":
        print("Hai scelto di uscire dal programma.")
    else:
        print("Scelta non valida, riprova.")
