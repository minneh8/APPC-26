n = 1
while (n == 1):  #Primeiro
    n1 = float(input("Digite um valor: "))
    n2 = float(input("Digite outro valor: "))
    print("Deseja digitar outro valor? se SIM! digite 1, se NÃO digite 2")
    n = int(input("Digite sua resposta: "))
    if n != 1:
        media = (n1 + n2) / 2
        nmax = max(n1, n2 )
        nmin = min(n1, n2 )
        print(f"O maior valor digitado foi: {nmax} e o menor foi: {nmin}")
        print("A media dos dois valores digitados é:", media)
        
    if n == 1:
        n3 = float(input("Digite outro valor: "))

    #Segundo
    print("Deseja digitar outro valor? se SIM! digite 1, se NÃO digite 2")
    n = int(input("Digite sua resposta: "))
    if n != 1:
        media = (n1 + n2 + n3 ) / 3
        nmax = max(n1, n2, n3 )
        nmin = min(n1, n2, n3 )
        print(f"O maior valor digitado foi: {nmax} e o menor foi: {nmin}")
        print("A media dos tres valores digitados é:", media)
    if n == 1:
        n4 = float(input("Digite outro valor: "))

    #Terceiro
    print("Deseja digitar outro valor? se SIM! digite 1, se NÃO digite 2")
    n = int(input("Digite sua resposta: "))
    if n != 1:
        media = (n1 + n2 + n3 + n4) / 4
        nmax = max(n1, n2, n3, n4 )
        nmin = min(n1, n2, n3, n4 )
        print(f"O maior valor digitado foi: {nmax} e o menor foi: {nmin}")
        print("A media dos tres valores digitados é:", media)
    if n == 1:
        n5 = float(input("Digite outro valor: "))
    
    #Quarto
    print("Deseja digitar outro valor? se SIM! digite 1, se NÃO digite 2")
    n = int(input("Digite sua resposta: "))
    if n != 1:
        media = (n1 + n2 + n3 + n4) / 4
        print("A media dos quadro valores digitados é:", media)
    if n == 1:
        n5 = float(input("Digite outro valor: "))
        media = (n1 + n2 + n3 + n4 + n5) / 5
        nmax = max(n1, n2, n3, n4, n5)
        nmin = min(n1, n2, n3, n4, n5)
        print("A media dos cinco valores digitados é:", media)
        print(f"O maior valor digitado foi: {nmax} e o menor foi: {nmin}")
    n = 2

