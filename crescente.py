num1, num2, num3 = input("Informe 3 valores: ").split()
num1, num2, num3 = float(num1), float(num2), float(num3)

if (num1 > num2 > num3):
    print(num1, num2, num3)
if (num1 > num2 < num3):
    print(num1, num3, num2)
if (num2 > num1 > num3):
    print(num2, num1, num3)
if (num3 > num2 > num1):
    print(num3, num2, num1)
if (num3 > num2 < num1):
    print(num3, num1, num2)