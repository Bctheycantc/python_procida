nomeUtente = "Paolo Procida"
# utilizzo il simbolo "+" per concatenare delle stringhe, poi lo stampo 
presentazione = "Ciao, "+ nomeUtente +", questa è la calcolatrice più semplice"

print(presentazione)

numero1 = 42.3
numero2 = 6.4

# Calcolare le 4 operazioni matematiche di base
add = numero1 + numero2
prod = numero1 * numero2
sottr = numero1 - numero2
divis = numero1 / numero2

print("La somma vale ", add)
print("Il prodotto vale ", prod)
print("La sottrazione vale ", sottr)
print("Il quoziente vale ", divis)

# Elevamento a potenza
# Metodo 1, eleviamo alla seconda entrambi i numeri
potenza1 = numero1 ** 2
potenza2 = numero2 ** 2

print("La potenza del primo numero vale ", potenza1)
print("La potenza del secondo numero vale ", potenza2)

# Calcolo la radice quadrata utilizzando le potenze
radice1 = numero1 ** 0.5
radice2 = numero2 ** 0.5

print("La radice del primo numero vale ", radice1)
print("La radice del secondo numero vale ", radice2)

# Metodo 2, pow
numero3 = 4
potenza3 = pow(numero3, 2)

print("La potenza del terzo numero vale ", potenza3)

# Calcolo la radice quadrata utilizzando math
# Devo importare la libreria math, sono delle librerie di utilità matematica
# ATT: di solito quando si importano le librerie, devo importarle in alto alla pagina
import math
radice3 = math.sqrt(numero3)

print("La radice del terzo numero vale ", radice3)