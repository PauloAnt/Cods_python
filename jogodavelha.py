import os
import random
import colorama
from colorama import Fore, Back, Style

jogarnovamento = "s"
jogadas = 0
jogadores = 2
maxjogadas = 9
win = "n"
velha = [
    [" "," "," "]
    [" "," "," "]
    [" "," "," "] 
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    1  2  3")
    print("1:  " + velha[0][0] + "|" + velha [0][1] + "|" + velha[0][2])
    print("   -----------")
    print("2:  " + velha[1][0] + "|" + velha [1][1] + "|" + velha[1][2])
    print("   -----------")
    print("3:  " + velha[2][0] + "|" + velha [2][1] + "|" + velha[2][2])
    print("Jogadas: " + Fore.GREEN str(jogadas) + Fore.RESET)
