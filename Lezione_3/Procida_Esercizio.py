# Dichiaro il mio nome e cognome in due variabili
mioNome = "Paolo"
mioCognome = "Procida"

# Stampo il mio nome e cognome
print("Ciao, " + mioNome + " " + mioCognome)

# Calcola l'area e il perimetro di un rettangolo avente base 5,7 e altezza 6,2
# Dichiaro le dimensioni del rettangolo
baseRettangolo = 5.7
altezzaRettangolo = 6.2
# Calcolo l'area del rettangolo
areaRettangolo = baseRettangolo * altezzaRettangolo
# Calcolo il perimetro del rettangolo
perimetroRettangolo = (baseRettangolo + altezzaRettangolo) * 2

# Stampo i risultati
print("L'area del rettangolo è ", areaRettangolo)
print("Il perimetro del rettangolo è ", perimetroRettangolo)

# Calcola l'area e il perimetro del seguente triangolo rettangolo dove lato1 = 9 lato2 = 12 lato3 = 15 e calcola il teorema di Pitagora
# Dichiaro le dimensioni del triangolo
lato1Triangolo = 9
lato2Triangolo = 12
lato3Triangolo = 15
# Calcolo l'area del triangolo
areaTriangolo = lato1Triangolo * lato2Triangolo / 2
# Calcolo il perimetro del triangolo
perimetroTriangolo = lato1Triangolo + lato2Triangolo + lato3Triangolo
# Calcolo Pitagora
pitagora = (lato1Triangolo ** 2 + lato2Triangolo ** 2) ** 0.5

# Stampo i risultati
print("L'area del triangolo è", areaTriangolo)
print("Il perimetro del triangolo è", perimetroTriangolo)
print("L'ipotenusa secondo il teorema di Pitagora è", pitagora)

# Calcola l'area e il perimetro di un cerchio di raggio 8.7 (Usa entrambi i metodi per il calcolo della potenza)
# Dichiaro il raggio del cerchio e il valore del pi greco
raggioCerchio = 8.7
PI_GRECO = 3.141
# Calcolo l'area del cercio
areaCerchio = (raggioCerchio * PI_GRECO) ** 2
areaCerchio2 = pow(raggioCerchio * PI_GRECO, 2)
# Calcolo il perimetro del cerchio 
circonferenzaCerchio = raggioCerchio * PI_GRECO * 2
# Stampo i risultati
print("L'area del cerchio è", areaCerchio)
print("L'area del cerchio utilizzando pow è", areaCerchio2)
print("Il perimetro del cerchio è", circonferenzaCerchio)