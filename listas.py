'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

import time

notas = []

print("Informe várias notas que darei algumas informações sobre elas.\nDigite algum valor abaixo de (0) para sair.")

valores = int(input("R: "))
notas.append(valores)

while (valores > 0):
    valores = int(input("R: "))
    notas.append(valores)
    if 0 in notas:
        notas.remove(0)

    
print(f"Quantidade de valores informados: {len(notas)}")
notas.sort()
print(f"Valores na ordem crescente: {notas}")
notas.sort(reverse=True)
print("Valores na ordem decrescente: ", *notas, sep="\n")

soma = 0
cont = 0
maior_med = []
menor_med = []

for nota in notas:
    soma += nota
    cont += 1
    media = soma / cont

for nota in notas:
    if (nota > media):
        maior_med.append(nota)
    elif (nota < 7):
        menor_med.append(nota)

print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media}")
print(f"Acima da média: {maior_med}")
print(f"Abaixo da média: {menor_med}")

print("Programa encerrando em 5 segundos.")

print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

print("Programa encerrado.")