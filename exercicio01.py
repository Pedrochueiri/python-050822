#calculadora simples
#operações :adição, subtração, multiplicação e divisão

#menu()
#entrada_de_dados()
#adicao()
#subtracao()
#multiplicacao()
#divisao()
#imprimir()
#controlador()

#função menu()
from unittest import result


def menu():
    print("*- Menu -*")
    print("1-Adição")
    print("2-Subtração")
    print("3-multiplicação")
    print("4-Divisão")
    op = int(input("Operação: "))
    return op

#------------------------------------------------
#Função entrada_de_dados()
def entrada_de_dados():
    print("*- Entrada de Dados -*")
    num = int(input("Número: "))
    return num

#------------------------------------------------
#função adição()
def adicao(n1,n2):
    print("*- Adição -*")
    result = n1 + n2
    return result

#------------------------------------------------
#função subtração()
def subtracao(n1,n2):
    print("*- Subtração -*")
    result = n1 - n2
    return result

#------------------------------------------------
#função multiplicação()
def multiplicacao(n1,n2):
    print("*- Multiplicação -*")
    result = n1 * n2
    return result

#------------------------------------------------
#função divisão()
def divisao(n1,n2):
    print("*- Divisão -*")
    result = n1 / n2
    return result

#------------------------------------------------
#função inprimir()
def imprimir(result):
    print("*- Imprimir -*")
    print("Resultado: ", result)

#------------------------------------------------
#função controlador()
def controlador(n1,n2,op):
    print("*- Controlador -*")
    if op == 1:
        result = adicao(n1,n2)
    elif op == 2:
        result = subtracao(n1,n2)
    elif op == 3:
        result = multiplicacao(n1,n2)
    elif op == 4:
        result = divisao(n1,n2)
    else:
        result = "Opção inválida"
    return result