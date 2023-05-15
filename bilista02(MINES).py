matriz = [["X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X"]]
x= y = 0
cod = 1
print("\nMINES! Conte com sua sorte e escolha a posição certa para não cair na bomba...")
print("Informe as coordenadas de 0 a 4. Exemplo: 2 2\n")
for l in range(0, 5):
    for c in range(0, 5):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

while (cod == 1):
    x, y = input("Informe X e Y: ").split()
    x, y = int(x), int(y)
    if (x > 4) or (x < 0) or (y > 4) or (y < 0):
        print("Coordernada inválida... Informe novamente")
        cod = 2
        while (cod == 2):
            x, y = input("Informe X e Y: ").split()
            x, y = int(x), int(y)
            if (x > 4) or (x < 0) or (y > 4) or (y < 0):
                print("Coordernada inválida... Informe novamente")
                cod = 2
            else:
                cod = 1

    matriz[x][y] = "O"
    for l in range(0, 5):
        for c in range(0 ,5):
            print(f"[{matriz[l][c]:^5}]", end="")
        print()
    if (x == 0) and (y == 1) or (x == 2) and (y == 2) or (x == 4) and (y == 0):
        print("BOMBA! Você perdeu...")
        cod = 2