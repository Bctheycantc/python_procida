# Permetti all'utente di insierire 2 numeri interi e calcola il risultato delle seguenti operazioni
# +, -, *, /, **2

print("-------------CALCOLATRICE-------------")

num1=int(input("Inserisci il primo numero:"))
num2=int(input("Inserisci il secondo numero:"))

somma = num1 + num2
sottr = num1 - num2
moltipl = num1 * num2
divis = num1 / num2
potenza1 = num1 **2
potenza2 = pow(num2, 2)

print("La somma è:", somma)
print("La differenza è:", sottr)
print("Il prodotto è:", moltipl)
print("Il quoziente è:", divis)
print("Il quadrato del primo numero è:", potenza1)
print("Il quadrato del secondo numero (con pow) è:", potenza2)