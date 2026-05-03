n = int(input("Quantos alunos? "))
matriz = []
i = 0
while i < n:
    ra = int(input(f"\nDigite o RA do aluno {i+1}: "))
    linha = [ra, 0, 0, 0, 0, 0]
    j = 1
    while j <= 4:
        linha[j] = float(input(f"  Nota {j}: "))
        j += 1
    linha[5] = (linha[1] + linha[2] + linha[3] + linha[4]) / 4
    matriz.append(linha)
    i += 1

print(f"\n{'RA':<10} {'NOTA1':<8} {'NOTA2':<8} {'NOTA3':<8} {'NOTA4':<8} {'MEDIA':<8}")
i = 0
while i < n:
    linha = matriz[i]
    print(f"{int(linha[0]):<10} {linha[1]:<8.1f} {linha[2]:<8.1f} {linha[3]:<8.1f} {linha[4]:<8.1f} {linha[5]:<8.2f}")
    i += 1
print()