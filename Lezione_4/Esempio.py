# Esempio di dichiarazione e uso variabili
print("Scrivi il tuo nome, caro utente:")

# Per poter acquisira qualcosa che digita l'utente, utilizzo la funzione input()
nomeUser=input()

# print("Benvenuto, ",nomeUser)

# Facendo la stessa cosa in modo più veloce passando come argomento all'input una frase
cognomeUser=input("Scrivi il tuo cognome: ")
print("Benvenuto, ",nomeUser,cognomeUser)

# esempio con int
print("------------SOMMA------------")
num1 = int(input("Scrivi il primo numero: "))
num2 = int(input("Scrivi il secondo numero: "))
somma = num1 + num2
print("La somma dei due numeri è", somma)

