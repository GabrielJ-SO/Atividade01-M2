
def menu():
    print("\tMenu de opções:")
    print(".1 - Bonus salario")
    print(".2 - identificador de triângulo")
    print(".3 - IMC")
    print(".4 - Calculo de Média")
    print(".5 - Verificador de data valida")
    print(".6 - Verifica condição de voto")
    print(".7 - Classificador de risco")
    print(".8 - Jogo de adivinhação")
    print(".9 - Desconto para cliente VIP")
    print(".10 - Validador de senha")
    print(".0 - Sair")
    opcao = str(input("Digite a opção desejada: "))

    return opcao

def CalculoBonusSalario(salario, tempo):


    if salario < 2000 and tempo >= 5:
        bonus = salario * 0.2

    elif salario < 2000 and tempo < 5:
        bonus = salario * 0.1

    elif salario >= 2000 and tempo >= 5:
        bonus = salario * 0.05

    elif salario >= 2000 and tempo < 5:
        bonus = salario * 0
    
    else:
        salario = salario * 0

    salario += bonus

    print("O seu salário é:", salario)