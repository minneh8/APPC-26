# Ler o número
valor = int(input("Digite um número: "))
contador = valor
fatorial = 1
while (contador > 1):
    fatorial = fatorial * contador
    contador = contador - 1

print("O fatorial de", valor , "é:", fatorial)