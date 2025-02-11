import math

binario = input("Digite o valor Binário: ")

if not all(d in "01" for d in binario):
    print("Erro: Digite apenas números binários (0 e 1).")
    exit()

quantidade = len(binario) - 1
resultado = 0

for i, digito in enumerate(binario):
    elevado = math.pow(2, quantidade - i)
    resultado += int(digito) * elevado

print(f"Decimal: {int(resultado)}")
