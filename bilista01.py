import random

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("Informe números para preencher a matriz.")
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = random.randint(1, 1000)
print("-=" * 50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()

print("-=" * 50)

import random
import numpy as np

# Criar o array 3 x 3 com números aleatórios entre 1 e 52
x = np.random.randint(1,1000, (3,3))

print(x)