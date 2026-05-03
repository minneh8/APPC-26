n = int(input("Quantos valores deseja digitar? "))
vetor = []
i = 0
while i < n:
    valor = float(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)
    i += 1

maior = vetor[0]
menor = vetor[0]
soma = 0
i = 0
while i < n:
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
    soma += vetor[i]
    i += 1

media = soma / n
print(f"\nMaior: {maior}")
print(f"Menor: {menor}")
print(f"Media: {media:.2f}\n")