import sys

sys.stdout.reconfigure(encoding='utf-8')

numeros = [10, 20, 30, 40, 50]


soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)
print("A média dos números é:", media)