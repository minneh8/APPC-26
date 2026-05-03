n = int(input("Quantos alunos? "))
matriz = []
medias = []
i = 0
while i < n:
    ra = int(input(f"\nDigite o RA do aluno {i+1}: "))
    notas = []
    j = 0
    while j < 4:
        nota = float(input(f"  Nota {j+1}: "))
        notas.append(nota)
        j += 1
    soma = notas[0] + notas[1] + notas[2] + notas[3]
    matriz.append([ra, notas[0], notas[1], notas[2], notas[3]])
    medias.append(soma / 4)
    i += 1

    print(f"\n{'RA':<10} {'NOTA1':<8} {'NOTA2':<8} {'NOTA3':<8} {'NOTA4':<8} {'MEDIA':<8}")
i = 0
while i < n:
    ra = matriz[i][0]
    n1 = matriz[i][1]
    n2 = matriz[i][2]
    n3 = matriz[i][3]
    n4 = matriz[i][4]
    print(f"{ra:<10} {n1:<8.1f} {n2:<8.1f} {n3:<8.1f} {n4:<8.1f} {medias[i]:<8.2f}")
    i += 1
print()
