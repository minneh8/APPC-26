#Apresentar os caracteres de uma string
#Apresentar as vogais e as consoantes
frase = input("Digite uma frase: ")
vogais = " "
consoantes = " "
nchar = len(frase)
pos = 0
while(pos < nchar):
    print("pos = ", pos, "\t ", frase[pos])
    if frase[pos] == "a" or frase[pos] == "e" or frase[pos] == "i" or frase[pos] == "o" or frase[pos] == "u":
       vogais = vogais + frase[pos]
    else: 
        consoantes = consoantes + frase[pos]
    pos = pos + 1
print(f"VOGAIS: {vogais}")
print(f"CONSOANTES: {consoantes}")