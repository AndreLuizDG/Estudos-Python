
resposta = ''
l, r = 0, 0

frase = input('Digite a palavra:')


while r < len(frase):
    if frase[r] != ' ':
        r += 1
    else:
        resposta += frase[l:r+1][::-1]
        r += 1
        l = r
resposta += ' '
resposta += frase[l:r+1][::-1]

print (resposta[1:])
