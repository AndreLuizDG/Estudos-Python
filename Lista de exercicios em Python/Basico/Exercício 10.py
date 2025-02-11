import sys
sys.stdout.reconfigure(encoding='utf-8')

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def retorna_letra(indice):
    print(f"A letra do índice é: {abc[indice]}")

indice = int(input("Digite um indice:"))
retorna_letra(indice - 1)
