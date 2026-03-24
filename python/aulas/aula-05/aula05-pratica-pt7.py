#Apresentar os caracteres de uma string
#        012345
frase = input("Digite uma frase = ")
nchar = len(frase)
contvogal = 0
contbranco = 0
pos = 0
while(pos < nchar):
    print("pos = ", pos, "\t ", frase[pos])
    if frase[pos] == " ":
        contbranco = contbranco  + 1 
    if frase[pos] == "a" or frase[pos] == "e" or frase[pos] == "i" or frase[pos] == "o" or frase[pos] == "u":
        contvogal = contvogal + 1 
    pos = pos + 1
print(f"Numero de Vogais é igual a {contvogal}")
print(f"Numero de espaços em branco é igual a {contbranco}")