n = int(input("Digite o numero de linhas (N): "))

linha = 1
while linha <= n:
    qtd_estrelas = (2 * linha) - 1
    qtd_espacos = n - linha

    espacos = ""
    k = 0
    while k < qtd_espacos:
        espacos += " "
        k += 1

    estrelas = ""
    k = 0
    while k < qtd_estrelas:
        estrelas += "*"
        k += 1

    print(espacos + estrelas)
    linha += 1
print()