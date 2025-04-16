# Liste

# 0 based, la conta parte da 0
miaLista = ["mela", "pesca", "banana", "kiwi"]

for frutto in miaLista:
    print(frutto)

# Fornisco la lista dei miei voti, tutte le volte che incotro un voto insufficiente stampo un avviso
voti = [100, 50, 25, 85, 20]

for voto in voti:
    if voto <= 50:
        print("Attenzione,", voto, "e' insufficiente")
    else:
        print("Voto:", voto)