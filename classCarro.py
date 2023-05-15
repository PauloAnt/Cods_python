class Carros:
    def __init__(self, cor, marca, valor, nome):
        self.cor = cor
        self.marca = marca
        self.valor = valor
        self.nome = nome

    def pedal(self, escolha_pedal):
        pedais = ["esquerda", "meio", "direita"]
        escolha_pedal = input("\nEscolha o pedal:\n1- Esquerda\n2- Meio\n3- Direita\n\nR: ").lower()
        if (escolha_pedal not in pedais):
            while True:
                if (escolha_pedal not in pedais):
                    print("Pedal inválido")
                    escolha_pedal = input("\nEscolha o pedal:\n1- Esquerda\n2- Meio\n3- Direita\n\nR: ").lower()
                else:
                    break
        
        if (escolha_pedal == "esquerda"):
            print("Você pisou na embreagem")
        elif (escolha_pedal == "meio"):
            print("Você freiou")
        elif (escolha_pedal == "direita"):
            print("Você acelelerou")


carro1 = Carros("Preto", "Hyundai", "50.000", "HB20")
carro2 = Carros("Cinza", "Honda", "40.000", "Civic")
print(carro1.cor, carro2.cor)
print(carro1.marca, carro2.marca)
print(carro1.valor, carro2.valor)
print(carro1.nome, carro2.nome)

carro1.pedal(escolha_pedal="")

