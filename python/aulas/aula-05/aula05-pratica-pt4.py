import random
#Gerar um numero aleatorio entre [0, 99]
#random.uniform(valor inicial, valor final)
#random.uniform(0,99)
random.seed
numerocomputador = int(random.uniform(0, 99))
numerojogador = -1
while (numerojogador != numerocomputador):    
    numerojogador = int(input("Digite seu numero: "))
    if (numerojogador > numerocomputador):
        print("Seu numero é maior, tente novamente")
    elif (numerojogador < numerocomputador):
        print("Seu numero é menor, tente novamente")
    elif (numerojogador == numerocomputador):
        print("Parabens, vocé acertou")