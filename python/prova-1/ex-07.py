while True :
    try:
        nf = int(input("Digite o número de participantes da pesquisa: "))
        if nf > 0 :    
            print(f"Participantes: {nf}")
            print("-------------------------------------------------------")
            break
        else: 
            print("Digite um valor maior que 0.")
    except:
        print("Entrada inválida!")

idademin = 10000
idademax = 0
somaidade = 0
somaA = 0
somaM = 0
somaC = 0
i = 0
while i <nf :
    print(f"Participante {i+1}")

    while True: 
        idade = int(input("Digite a idade: "))
        if idade > 0:
            break
        else:
            print("Digite uma idade maior que 0.")

    while True:
        print ("A - Aventura (Tirolesa, escalada, bungee jump e boia) / M - Montanha Russa / C - Clássicos (Patinação, Cavalgada e Charrete) ")
        atividade = input("Digite a atividade:  ").upper()
        if atividade == "A":
            somaA = somaA + 1
            print("A atividade escolhida foi Aventura")
        elif atividade == "M":
            somaM = somaM + 1
            print("A atividade escolhida foi Montanha Russa")
        elif atividade == "C":
            somaC = somaC + 1
            print("A atividade escolhida foi Clássicos")
        else: 
            print("Atividade inválida!")
        break

    print("Participante", i+1, "com idade", idade, "e atividade", atividade)
    print("-------------------------------------------------------")
    i = i + 1
    somaidade = somaidade + idade
    if idade < idademin:
        idademin = idade
    if idade > idademax:
        idademax = idade


idademedia =  somaidade / nf
somatotal = somaA + somaM + somaC
porcA = (somaA / somatotal) * 100
porcM = (somaM / somatotal) * 100
porcC = (somaC / somatotal) * 100

print("RESULTADO : ")
print("-------------------------------------------------------")
print("O participante mais novo tem", idademin, "anos")
print("O participante mais velho tem", idademax, "anos")
print("A idade média dos participantes foi", idademedia)
print("-------------------------------------------------------")
print("O percentual de participantes que escolheram Aventura foi de", porcA, "%")
print("O percentual de participantes que escolheram Montanha Russa foi de", porcM, "%")
print("O percentual de participantes que escolheram Clássicos foi de", porcC, "%")







    