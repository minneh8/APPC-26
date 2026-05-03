n = int(input("Quantos valores deseja digitar? "))
vetor = []
i = 0
while i < n:
    valor = float(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)
    i += 1

print("\nVetor na ordem inversa:")
pos = n - 1
while pos >= 0:
    print(vetor[pos])
    pos -= 1
print()