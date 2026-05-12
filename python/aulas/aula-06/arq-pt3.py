dados = [
    ['Lucas', 18, '1999299232', 'lucas@gmai.com'], 
    ['Zago', 19, '19929938123', 'zago@gmail.com'], 
    ['guibus', 22, '10298378291', 'guibus@gmail.com'],
    ['Adamastor', 23, '10298378291', 'adamastor@gmail.com']
    ]

arquivo = open("dados.txt" , "w")

for reg in dados:
    #Armazenar os dados
    arquivo.write(f"Nome: {reg[0]}\n")
    arquivo.write(f"Idade: {reg[1]}\n")
    arquivo.write(f"Celular: {reg[2]}\n")
    arquivo.write(f"Email:{reg[3]}\n \n")