import sys
sys.stdout.reconfigure(encoding='utf-8')


palavra = "Radar"

palavra = palavra.lower()

palavra_inv = palavra[::-1]

if palavra_inv == palavra:
    print(f"{palavra} é um palindromo.")
else:
    print(f"{palavra} não é um palindromo.")