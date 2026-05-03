n = int(input("Quantos valores deseja digitar? "))
vetor = []
i = 0
while i < n:
    valor = float(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)
    i += 1

print(f"\nVetor original: {vetor}")
vetor.sort()
print(f"Vetor ordenado: {vetor}\n")