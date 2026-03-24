#Apresentar os caracteres de uma string
#Desenvolver uma aplicação de software para ler uma frase, contendo espaços em branco e remove-los
frase = input("Digite uma frase: ")
contbranco = ""
resto = ""
nchar = len(frase)
pos = 0
while(pos < nchar):
    print("pos = ", pos, "\t ", frase[pos])
    if frase[pos] == " ": 
        contbranco = contbranco + frase[pos]
    else: 
        resto = resto + frase[pos]
    pos = pos + 1
print(f"A frase em os espaços fica: {resto}")