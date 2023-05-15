import time

numeros = []
pares = []

print("Para sair escreva (0)")
while True:
    numero = int(input("Digite numeros: "))
    if (numero == 0):
        break
    numeros.append(numero)

for i in numeros:
    if (i % 2 == 0):
        pares.append(i)

print("Os pares: ", pares)

print("=-" * 50)

time.sleep(1)
vogais = ["a", "e", "i", "o", "u", "á", "ã", "â", "é", "ê", "í", "ó", "ô", "ú"]

cont_vogal = 0
cont_cons = 0
cont_letra = 0
cont_palavra = 1

print("Informe uma palavra ou frase que direi quantas palavras, letras, vogais e consoantes ela possui.")
palavra = input("R: ").lower()

for i in range(0, len(palavra)):
    if (palavra[i] in vogais):
        cont_vogal += 1
    elif (palavra[i] == " "):
        cont_palavra += 1
    elif (palavra[i] not in vogais):
        cont_cons += 1

cont_letra = cont_cons + cont_vogal

print(f"Palavra(s): {cont_palavra}\nLetra(s): {cont_letra}\nVogais: {cont_vogal}\nConsoantes: {cont_cons}")



