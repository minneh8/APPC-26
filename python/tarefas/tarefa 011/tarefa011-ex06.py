numero = int(input("Digite um numero inteiro: "))
bits = []

n_aux = numero
while n_aux > 0:
    bits.insert(0, n_aux % 2)
    n_aux = n_aux // 2

binario = ""
i = 0
while i < len(bits):
    binario += str(bits[i])
    i += 1

print(f"\nValor:   {numero}")
print(f"Binario: {binario}")
print(f"Vetor:   {bits}\n")