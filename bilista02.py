import random
cont = 0
m = []
for l in range(4):
    linha = []
    for c in range(4):
        linha.append(random.randint(0, 30))
    m.append(linha)

for l in range(0, 3):
    for c in range(0, 3):
        if (m[l][c] >= 10):
            cont += 1
        print(f"[{m[l][c]:^4}]", end="")
    print()
print("Valores maior ou igual a 10:", cont)