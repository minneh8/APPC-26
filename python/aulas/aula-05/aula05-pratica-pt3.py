#Determinar o valor de cont e y, de tal forma obter o maior valor de ambos
ymax = -1000
contmax = -1000
cont = 0 
while(cont <= 10):
    y = -4 * cont ** 2 + 40 * cont 
    if (y > ymax):
        ymax = y
        contmax = cont
    cont = cont + 1
print(f"O valor maximo para o y é {ymax} e o valor de cont é {contmax}")