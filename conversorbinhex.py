
print("\nConversor de decimal para binário e hexadecimal.")

valor = int(input("Informe o valor decimal: "))

#binario = "{0:b}".format(valor)

print("Binário:", bin(valor).lstrip("0b"))
print("Hexadecimal: ", hex(valor).lstrip("0x").upper())

