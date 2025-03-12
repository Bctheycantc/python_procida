#il tuo nome
print("Inserisci il tuo nome:")
nome = input()
#il tuo saldo iniziale
saldo = 261
print("Benvenuto,",nome,". Il tuo saldo attuale è €",saldo,"\nQuanto desideri depositare?")
#quanto decidi di depositare
deposito = int(input()) 
#controlla che il deposito non sia superiore a 600, poi aggiunge il deposito al saldo
if deposito > 600:
    print("Spiacenti, il deposito non può superare i € 600.")
else:
    saldo += deposito
    print("Hai depositato €",deposito,". Il tuo nuovo saldo è €",saldo)