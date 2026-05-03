
n = int(input("Quantos nomes deseja cadastrar? "))
nomes = []
i = 0
while i < n:
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
    i += 1

print(f"\nNomes cadastrados: {nomes}")

consulta = input("\nDigite o nome que deseja consultar: ")
encontrado = False
i = 0
while i < len(nomes):
    if nomes[i].upper() == consulta.upper():
        encontrado = True
        break
    i += 1

if encontrado:
    print(f"'{consulta}' esta cadastrado!\n")
else:
    print(f"'{consulta}' NAO esta cadastrado.\n")