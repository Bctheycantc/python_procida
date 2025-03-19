# Instanziare una variabile "saldo" = 1000
# Chiede all'utuente quanto ha guadagnato questo mese (Utlizza float)
# Se l'utente ha guadagnato piu' di 1000 euro stampare: "Bravo, questo mese hai guadagnato bene". Calcolare quanto effettivamente ha guadagnato (Guadagno 1500, incasso (10000 + 15000) = 500)
# Se l'utente ha guadagnato meno di 1000 stampare: "Mi spiace, questo mese hai guadagnato cosi' cosi'". Calcolare il saldo su 1000 euro
# Se l'utente ha guadagnato 0 stampare: "Questo mese non hai guadagnato nulla". Calcolare il saldo
# Se l'utente e' andato in perdita, stampare: "Questo mese stai perdendo soldi". Calcolare il saldo

saldo = float(1000)

# Chiedere all'utente quanto ha guadagnato
guadagno = float(input("Ciao Utente,\nGuadagno di questo mese: "))

# Calcolare l'incasso
incasso = saldo + guadagno

if guadagno >= 1000:
    print("Bravo, questo mese hai guadagnato bene")
elif guadagno == 0:
    print("Questo mese non hai guadagnato nulla")
elif guadagno < 0:
    print("Questo mese stai perdendo soldi")
elif guadagno > 0:
    print("Mi spiace, questo mese hai guadagnato cosi' cosi'")

# Elenco il nuovo saldo
print("Il tuo nuovo saldo e':", incasso)