
while True:
    try:
        nf = int(input("Digite o número de funcionários: "))
        if nf > 0:
            break
        else:
            print("Digite um valor maior que 0.")
    except:
        print("Entrada inválida!")

foltotal = 0
texcedente = 0
qtdmin = 0
qtdacima = 0

i = 0  # contador

while i < nf:
    print(f"Funcionário {i+1}")

    while True:
        nivel = input("Digite o nível (N1, N2, N3): ").upper()
        if nivel in ["N1", "N2", "N3"]:
            break
        else:
            print("Nível inválido!")

    while True:
        try:
            producao = int(input("Digite a produção diária: "))
            if producao >= 0:
                break
            else:
                print("Produção não pode ser negativa.")
        except:
            print("Entrada inválida!")

    if nivel == "N1":
        sbase = 1000
        minimo = 20
        bonus = 100
    elif nivel == "N2":
        sbase = 3000
        minimo = 40
        bonus = 400
    else: 
        sbase = 7000
        minimo = 60
        bonus = 900

    if producao > minimo:
        excedente = producao - minimo
        acrescimo = excedente * bonus
        qtdacima += 1
    else:
        excedente = 0
        acrescimo = 0
        qtdmin += 1

    stotal = sbase + acrescimo

    foltotal += stotal
    texcedente += excedente

    print(f"Salário base: R$ {sbase:.2f}")
    print(f"Acréscimo: R$ {acrescimo:.2f}")
    print(f"Salário total: R$ {stotal:.2f}")

    i += 1  # incrementa o contador (ESSENCIAL)

percmin = (qtdmin / nf) * 100
percacima = (qtdacima / nf) * 100

print("RESULTADOS: ")
print(f"Folha total: R$ {foltotal:.2f}")
print(f"Total de peças excedentes: {texcedente}")
print(f"Funcionários na produção mínima: {qtdmin}")
print(f"Funcionários acima da produção mínima: {qtdacima}")
print(f"Percentual mínimo: {percmin:.2f}%")
print(f"Percentual acima: {percacima:.2f}%")