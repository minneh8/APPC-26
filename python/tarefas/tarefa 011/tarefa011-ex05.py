n = int(input("Quantos valores deseja digitar? "))
vetor = []
i = 0
while i < n:
    valor = float(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)
    i += 1

print(f"\nVetor original: {vetor}")

i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if vetor[j] > vetor[j + 1]:
            aux = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = aux
        j += 1
    i += 1

print(f"Vetor ordenado: {vetor}\n")