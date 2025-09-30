

def menu():
    """Exibe o menu e retorna a opção selecionada.
    
        Returns:
            str: A opção selecionada pelo usuário.
    """
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



def CalculoBonusSalario(salario, tempo) -> float:
   
    """Calcula o bônus salarial com base no salário e tempo de empresa.
    
    Args:
        salario (float): O salário atual do funcionário.
        tempo (int): O tempo de empresa em anos.

    Returns:
        float: O salário final com o bônus aplicado.
    """

    bonus = 0
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

    return salario



def IdentificadorTriangulo(lado1, lado2, lado3) -> str:
    """Identifica o tipo de triângulo com base nos comprimentos dos lados.
    
    Args:
        lado1 (float): Comprimento do primeiro lado.
        lado2 (float): Comprimento do segundo lado.
        lado3 (float): Comprimento do terceiro lado.

    Returns:
        str: O tipo de triângulo ("Equilátero", "Isósceles", "Escaleno" ou "Não é um triângulo").
    """

    if (lado1 + lado2 < lado3) or (lado2 + lado3 < lado1) or (lado1 + lado3 < lado2):
        return "Não é um triângulo"
    
    elif lado1 == lado2 and lado3 == lado1:
        return "Equilátero"
    
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        return "Escaleno"
    
    else:
        return "Isósceles"
    


def CalculadoraIMC(peso, altura) -> str:

    """Calcula o Índice de Massa Corporal (IMC) e classifica o resultado.
    
        Args:
            peso (float): O peso em quilogramas.
            altura (float): A altura em metros.

        Returns:
            str: A classificação do IMC.
    """

    imc = peso / (altura ** 2)

    if(imc < 18.5):
        return "Abaixo do peso"
    
    elif(imc >= 18.5 and imc < 25):
        return "Peso normal"
    
    elif(imc >= 25 and imc < 30):
        return "Sobrepeso"
    
    elif(imc >= 30 and imc < 35):
        return "Obesidade grau I"
    
    elif(imc >= 35 and imc < 40):
        return "Obesidade grau II"
    
    else:
        return "Obesidade grau III"



def CalculaMedia(notas) -> float:
    """Calcula a média de uma lista de notas.
    
        Args:
            notas (list of float): Lista contendo as notas.

        Returns:
            float: A média das notas.
    """
    media = 0
    for i in range(len(notas)):
        media += notas[i]

    media = media / len(notas)

    return media


