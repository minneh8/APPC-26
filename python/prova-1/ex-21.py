cadastros = 0
somaex = 0
somaidade = 0 
somapeso = 0
pesomax = -10000
pesomin = 10000
idademax = -10000
idademin = 10000
fzexS = 0
fzexN = 0
cont="S"
while cont=="S" or cont=="s":
    try:
        print("-------------------------------------------------------")
        idade = int(input("Digite a idade: "))
        peso = float(input("Digite o peso: "))
        fzex = ""
        while (fzex != "S" and fzex != "s" and fzex != "N" and fzex != "n"):
            fzex = input("Faz exercicio regularmente? (S/N): ")
            if fzex == "S" or fzex == "s":
                print("Cadastro realizado com sucesso")
                fzexS = fzexS + 1
            elif fzex == "N" or fzex == "n":
                print("Cadastro realizado com sucesso")
                fzexN = fzexN + 1
            elif fzex != "S" and fzex != "s" and fzex != "N" and fzex != "n":
                print("Por favor, digite S ou N")
                print("Vamos tentar novamente ")
        print("-------------------------------------------------------")
        

        somaex = somaex + fzexS
        somaidade = somaidade + idade
        somapeso = somapeso + peso

        if idade > idademax:
            idademax = idade

        if idade < idademin:
            idademin = idade

        if peso > pesomax:
            pesomax = peso

        if peso < pesomin:
            pesomin = peso
        cadastros = cadastros + 1
        cont = ""
        while cont != "N" and cont != "n" and cont != "S" and cont != "s":
            cont  = input("Quer continuar implementando dados ? (S/N): ")
            print("-------------------------------------------------------")
            if cont != "N" and cont != "n" and cont != "S" and cont != "s":
                print("Por favor, digite S ou N")
                print("Vamos tentar novamente ")
    except:
        print("Opss, Erro...")

mediaidade = somaidade / cadastros
mediapeso = somapeso / cadastros
percex = fzexS / cadastros * 100
percexN = fzexN / cadastros * 100
print(f"Quantidade de pessoas cadastradas: {cadastros}")
print(f"Media de idade das pessoas cadastradas: {mediaidade}")
print(f"Media de peso das pessoas cadastradas: {mediapeso}")
print(f"Pessoa mais velha cadastrada: {idademax}")
print(f"Pessoa mais nova cadastrada: {idademin}")
print(f"Peso mais alto cadastrado: {pesomax}")
print(f"Peso mais baixo cadastrado: {pesomin}")
print(f"Percentual de pessoas que fazem exercicio: {percex :.2f}")
print(f"Percentual de pessoas que nao fazem exercicio: {percexN :.2f}")

