arquivo = open("arquivo.txt", "r")
vl = " "
dados = []

while vl != "":
    vl = arquivo.readline()
    if vl != "":
        vl = int(vl)
        dados.append(vl)
arquivo.close

print(f"O numero minimo é {min(dados)}")
print(f"O numero maximo é {max(dados)}")
media = sum(dados) / len(dados)
print(f"A media é {media :0.2f}")