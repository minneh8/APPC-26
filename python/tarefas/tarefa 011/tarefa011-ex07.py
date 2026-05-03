import math

n_pontos = int(input("Quantos pontos tem a fazenda? "))
pontos = []
i = 0
while i < n_pontos:
    x = float(input(f"P{i} - X: "))
    y = float(input(f"P{i} - Y: "))
    pontos.append([x, y])
    i += 1

perimetro = 0
i = 0
while i < n_pontos:
    prox = (i + 1) % n_pontos
    dx = pontos[i][0] - pontos[prox][0]
    dy = pontos[i][1] - pontos[prox][1]
    dist = math.sqrt(dx**2 + dy**2)
    perimetro += dist
    i += 1

print(f"\nPerimetro da fazenda: {perimetro:.2f} unidades\n")