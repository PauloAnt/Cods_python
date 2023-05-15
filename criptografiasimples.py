import string
import random

#letterrandom = chr(random.randint(ord("A"), ord("Z")))
letrarandom = random.choice(string.ascii_letters)

print("\nCriptografe sua senha.")
password = input("Insira sua senha: ")
crips = []
for i in range(len(password) * 3):
    #letterrandom = chr(random.randint(ord("A"), ord("Z")))
    #print(letterrandon, end="")
    letrarandom = random.choice(string.ascii_letters)
    crips.append(letrarandom)


print("Criptografia: ", end="")
for crip in crips:
    print(crip, end="")
