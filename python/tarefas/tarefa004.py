sh = float(input("Digite o salario hora: "))
ht = float(input("Digite o numero de horas trabalhadas: "))
f = float(input("Digite o numero de filhos: "))

#Cálculo
sb = sh * ht
if f >= 3:
    ca = f * 10 / 100
    sp = sb + ca
else: 
    ca = f * 5 / 100
    sp = sb + ca

if sp >= 15000:
    ir = sp * 27.5 / 100
    sl = sp - ir
    print("O salario liquido é:", sl)
else:
    ir = 0
    sl = sp
    print("O salario liquido é:", sl)



    
