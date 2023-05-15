import sys

qnt1 = 0
qnt2 = 0
qnt3 = 0
qnt4 = 0
soma = 0
cod = 1

print("Deseja comprar algo? (1) para sim (2) para não")
dec_cod = int(input("R: "))

if(dec_cod == 2):
    sys.exit()
if(dec_cod != 1 and 2):
    print("Código inválido")
    sys.exit()

while (dec_cod == 1):
    print("(1) para escolher Refrigerante: R$ 4.00")
    print("(2) para escolher Hambúrguer: R$ 3,50")
    print("(3) para Batata Frita: R$ 8,50")
    print("(4) para Sobremesa: R$ 5,00")
    print("(5) para voltar.")

    cod = int(input("Informe o código: "))
    if(cod == 1):
        qnt1 = int(input("Informe a quantidade do produto: "))
        if (qnt1 <= 0):
            print("Quantidade inválida")
            dec_cod = 1
        qnt1 = qnt1 * 4.00
        soma += qnt1
    elif(cod == 2):
        qnt2 = int(input("Informe a quantidade do produto: "))
        if (qnt2 <= 0):
            print("Quantidade inválida")
            dec_cod = 1
        qnt2 = qnt2 * 3.50
        soma += qnt2
    elif(cod == 3):
        qnt3 = int(input("Informe a quantidade do produto: "))
        if (qnt3 <= 0):
            print("Quantidade inválida")
            dec_cod = 1
        qnt3 = qnt3 * 8.50
        soma += qnt3
    elif(cod == 4):
        qnt4 = int(input("Informe a quantidade do produto: "))
        if (qnt4 <= 0):
            print("Quantidade inválida")
            dec_cod = 1
        qnt4 = qnt4 * 5.00
        soma += qnt4
    elif (cod == 5):
        print("Deseja comprar algo? (1) para sim (2) para não ")
        dec_cod = int(input("R: "))
        if (dec_cod < 1) or (dec_cod > 2):
            print("Código inválido")
            sys.exit()
        if(dec_cod == 2):
            print(f"Total: R$ {soma:.2f}")
            sys.exit()
    elif (cod > 5) or (cod < 1):
        print("Esse código não existe.")
        print("Digite novamente.")
        dec_cod = 1
        


