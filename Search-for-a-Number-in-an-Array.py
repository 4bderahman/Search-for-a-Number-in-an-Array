
T = [0] * 10  

for i in range(10):
    T[i] = int(input(f"Entrez un entier pour la position {i + 1} : "))

n = int(input("Entrez un entier à rechercher : "))

c = 0 

for i in range(10):
    if T[i] == n:
        c = c + 1

if c > 0:
    print(f"{n} se trouve dans le tableau.")
else:
    print(f"{n} ne se trouve pas dans le tableau.")
