
d = 0
tmenor = 10000
dmenor = 0
while (d < 31):
    T = 0.011 * d ** 3 - 0.3 * d ** 2 + 0.04 * d

    if T < tmenor:
        tmenor = T
        dmenor = d
    d = d + 1 


print(f"O dia {dmenor} foi o que atintiu a menor temperatura {tmenor}")