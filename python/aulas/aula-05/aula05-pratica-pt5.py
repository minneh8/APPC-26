import random
#Gerar um numero aleatorio entre [0, 99]
#random.uniform(valor inicial, valor final)
#random.uniform(0,99)
#seed = reinicializar o gerador de numeros randomicos!
random.seed
numerocomputador = int(random.uniform(0, 99))
numerojogador = -1
tentativas = 0
while (numerojogador != numerocomputador):    
    numerojogador = int(input("Digite seu numero: "))
    tentativas = tentativas + 1
    if (numerojogador > numerocomputador):
        print("Seu numero é maior que o desejado, tente novamente")
    elif (numerojogador < numerocomputador):
        print("Seu numero é menor que o desejado, tente novamente")
    elif (numerojogador == numerocomputador):
        print(f"Parabens, vocé acertou e o numero de tentativas é de {tentativas}")