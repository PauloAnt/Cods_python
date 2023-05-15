'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
'''
print("Qual o melhor Sistema Operacional para uso em servidores?")
print("0- Sair\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n")

votos = []
cod = 1
total = 0
cont_win = 0
cont_uni = 0
cont_lin = 0
cont_net = 0
cont_mac = 0
cont_out = 0

cod_sys = int(input("R: "))
if(cod_sys < 0) or (cod_sys > 6):
    cod == 2
else:
    votos.append(cod_sys)

while (cod == 1):
    if (cod_sys == 0):
        break
    elif(cod_sys <= 0) or (cod_sys > 6):
        print("Qual o melhor Sistema Operacional para uso em servidores?")
        print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n")
        print("Código inválida, insira novamente.")
        cod_sys = int(input("R: "))
        cod == 2
    else:
        print("Qual o melhor Sistema Operacional para uso em servidores?")
        print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n")
        cod_sys = int(input("R: "))
        votos.append(cod_sys)
for voto in range(0, len(votos)):
    if (voto == 1):
        cont_win += 1
    elif (voto == 2):
        cont_uni += 1
    elif (voto == 3):
        cont_lin += 1
    elif (voto == 4):
        cont_net += 1
    elif (voto == 5):
        cont_mac += 1
    elif (voto == 6):
        cont_out += 1
    cod == 1

while (cod == 2):
    if (cod_sys == 0):
        break
    elif(cod_sys < 0) or (cod_sys > 6):
        print("Qual o melhor Sistema Operacional para uso em servidores?")
        print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n")
        print("Código inválida, insira novamente.")
        cod_sys = int(input("R: "))
        cod == 2
    else:
        cod == 1


total = cont_mac + cont_lin + cont_net + cont_out + cont_uni + cont_win
print(  f"Sistema Operacional     Votos   %")
print(   "-------------------     -----  ---")
print(  f"Windows Server            {cont_win}    {(cont_win * 100)/total:.0f}%")
print(  f"Unix                      {cont_uni}    {(cont_uni * 100)/total:.0f}%")
print(  f"Linux                     {cont_lin}    {(cont_lin * 100)/total:.0f}%")
print(  f"Netware                   {cont_net}    {(cont_net * 100)/total:.0f}%")
print(  f"Mac OS                    {cont_mac}    {(cont_mac * 100)/total:.0f}%")
print(  f"Outro                     {cont_out}    {(cont_out * 100)/total:.0f}%")
print(   "-------------------     -----")
print(  f"Total                     {total}")






