n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

nmax = max(n1, n2)
nmin = min(n1, n2)

while (nmin  < nmax):
    nmin = nmin + 1
    print(f"VALORES DO INTERVALO ENTRE O {n1}, E O {n2}:")
    print(f"x = {nmin}")