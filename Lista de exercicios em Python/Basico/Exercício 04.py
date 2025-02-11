import sys
sys.stdout.reconfigure(encoding='utf-8')


palavras = ["python", "asimov", "código", "web", "programação"]

maior_palavra = len(palavras[0])
maior_palavra_txt = palavras[0]

menor_palavra = len(palavras[0])
menor_palavra_txt = palavras[0]



for palavra in palavras:
    if len(palavra) > maior_palavra:
        maior_palavra = len(palavra)
        maior_palavra_txt = palavra

    if len(palavra) < menor_palavra:
        menor_palavra = len(palavra)
        menor_palavra_txt = palavra

print(f"A maior palavra é: {maior_palavra_txt} {maior_palavra}")
print(f"A menor palavra é: {menor_palavra_txt} {menor_palavra}")