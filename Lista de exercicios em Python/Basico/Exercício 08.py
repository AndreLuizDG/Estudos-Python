import sys
sys.stdout.reconfigure(encoding='utf-8')


aumento_vendas = 32.048701

aumento_formatado = "{:.2f}".format(aumento_vendas)
print(f"O aumento percentual de vendas foi de {aumento_formatado}%")