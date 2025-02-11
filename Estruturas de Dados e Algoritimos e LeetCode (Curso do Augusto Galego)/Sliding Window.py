def MaiorTamanhoSubString(string: str) -> int:
    direita, esquerda = 0, 0
    _maximo = 1
    contador = {string[0]: 1}

    while direita < len(string) - 1:
        direita += 1
        contador[string[direita]] = contador.get(string[direita], 0) + 1

        while contador[string[direita]] == 3:
            contador[string[esquerda]] -= 1
            esquerda += 1

        _maximo = max(_maximo, direita - esquerda + 1)

    return _maximo


print(MaiorTamanhoSubString("abcabcbb"))
print(MaiorTamanhoSubString("aabbaacc"))
print(MaiorTamanhoSubString("abcde"))

