#Funzioni built-in
print("Prima funzione 'Built-in'")

print("Inserisci il tuo nome:")
#input() è una funzione built-in che mi permette di ricevere un valore e registrarlo in una variabile 
nome = input()
print("Ciao,", nome)

saldo = 1000
print("Benvenuto,",nome,"\nQuanto desideri prelevare?")
prelievo = int(input()) 
if prelievo > saldo:
    print("L'importo non può superare il saldo.")
else:
    saldo -= prelievo
    print("Hai prelevato €",prelievo,". Il tuo nuovo saldo è €",saldo)