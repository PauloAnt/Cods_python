import random
matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        linha.append(random.randint(0, 50))
    matriz.append(linha)
print("Lista origem:")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^4}]", end="")
    print()
print()
print("Lista multiplicada por 5:")
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] *= 5
        print(f"[{matriz[l][c]:^5}]", end="")
    print()