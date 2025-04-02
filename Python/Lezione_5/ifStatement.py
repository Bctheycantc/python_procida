# If Statement serve ad operare delle scelte in base alle condizioni

# SINTASSI
# if condizione:
#   esegui  se condizione [true]
# else :
#   esegui se condizione [false]

x = 10
y = 9

if x == y:
    print("I due numeri sono uguali")
else:
    print("I due numeri sono diversi")

# Introduzione
print("CONFRONTO TRA DUE NUMERI")
# Leggi i due numeri inseriti dall'utente
num1 = int(input("Inserisci il primo numero:"))
num2 = int(input("Inserisci il secondo numero:"))

if num1 > num2:
    print("Il primo numero e' piu' grande")
elif num1 < num2:
    print("Il secondo numero e' piu' grande")
elif num1 == num2:
    print("I due numeri sono uguali")
else:
    print("Non posso interpretare i tuoi numeri")