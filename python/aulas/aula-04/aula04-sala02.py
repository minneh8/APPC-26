try :
    x = float(input("Digite o valor de x: "))
    y = (4 + x ** 2 - 3 * x + 9) / x
    print("O valor de y é:",y)
except ValueError:
    print("Erro: O valor tem que ser numerico!")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
