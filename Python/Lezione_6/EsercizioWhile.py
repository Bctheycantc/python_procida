# Crea un programma che legge un numero inserito da un utente e stabilisce se questo numero e' pari o dispari, il programma si interrompe se l'utente inserisce il nunero "0"

print("-----PARI O DISPARI-----")

numero = ""

while numero != 0:

    numero = int(input("Inserire 0 per terminare il programma. \nInserisci un numero: \n"))
    if numero == 0:
        print("Il tuo numero e' 0. Termino programma.")
    elif numero  % 2 == 0:
        print("Il tuo numero e' pari.")
    else:
        print("Il tuo numero e' dispari.")

# Crea un programma per indovinare un numero segreto. Fino a quando l'utente non inserisce il numero corretto composto da 3 caratteri, il programma continuera' a dirgli che non e' possibile entrare. Ci sono un massimo di 4 tentativi

print("-----NUMERO SEGRETO-----")

numSegreto = 261
tentativi = 4

while tentativi > 0:
    print("Ti rimangono ", tentativi, "Tentativi")
    
    numIndovinato = int(input("Indovina il numero segreto di 3 cifre: \n"))
    if numIndovinato == numSegreto:
        print("Hai indovinato!, il numero e'", numSegreto, "!")
        tentativi = 0
    else:
        tentativi -= 1
        print("Il numero non e' corretto, riprova.")  
print("Hai chiuso il programma")