#Apresentar os caracteres de uma string
#Desenvolver uma aplicação de software para ler uma palavra e escrever ela invertida
frase = input("Digite uma palavra: ")
nchar = len(frase)
pos = nchar - 1
contrario = " "
while(pos >= 0):
    print("pos = ", pos, "\t ", frase[pos])
    contrario = contrario + frase[pos]
    pos = pos - 1
print(f"a palavra invertida fica: {contrario}")
