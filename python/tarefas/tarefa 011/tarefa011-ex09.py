n = int(input("Digite o numero de linhas (N): "))

linha = 1
while linha <= n:
    estrelas = ""
    k = 0
    while k < linha:
        estrelas += "*"
        k += 1
    print(estrelas)
    linha += 1
print()