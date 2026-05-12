arquivo = open("arquivo02.txt", "r")
vl = " "
dados = []
while vl != "":
    vl = arquivo.readline()
    if vl != "":
        #Ler nome
        vl = vl.split("\n")
        vl = vl[0]
        nome = vl
        #Ler idade
        vl = arquivo.readline()
        vl = vl.split("\n")
        vl = vl[0]
        idade = int(vl)
        #Ler celular
        vl = arquivo.readline()
        vl = vl.split("\n")
        vl = vl[0]
        celular = vl
        #Ler email
        vl = arquivo.readline()
        vl = vl.split("\n")
        vl = vl[0]
        email = vl
        aux = [nome, idade, celular, email]
        dados.append(aux)
arquivo.close()
print(dados)
