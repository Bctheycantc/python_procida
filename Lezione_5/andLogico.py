# Chiedi all'utente il nome, la sua eta' e se possiede l'invito

nome = input("Qual è il tuo nome? ")
eta = int(input("Quanti anni hai? "))
invito = input("Hai un invito? (y/n) ") == "y"

if eta >= 18 and invito:
    print("Ciao", nome, "puoi far parte del club.")
elif eta < 18 and invito:
    print("Caro", nome, "non hai ancora compiuto 18 anni. Anche se hai l'invito, non puoi entrare.")
elif eta >= 18 and not invito:
    print("Caro", nome, ", pur avendo 18 anni non puoi entrare poiché ti manca l'invito.")
else:
    print("Mi spiace", nome, ", non puoi far parte del club. Non hai 18 anni e non hai neanche un invito.")