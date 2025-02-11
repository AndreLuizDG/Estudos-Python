import sys
sys.stdout.reconfigure(encoding='utf-8')


numeros = [32, 10, 58, 30, 55, 12, 28, 51]

numeros.sort()
segundo_maior = numeros[-2]

print(f"O segundo maior numero é: {segundo_maior}")