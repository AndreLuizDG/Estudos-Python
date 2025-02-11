import sys

sys.stdout.reconfigure(encoding='utf-8')

nome = input("Nome:")
idade = input("Idade:")
cidade = input("Cidade:")

print(f"Olá! Meu nome é {nome}. Eu tenho {idade} anos e moro em {cidade}.")