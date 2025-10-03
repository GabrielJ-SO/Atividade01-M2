

import utils

def exercicio01() -> None:
    """ Executa o exercício 1 - Cálculo de bônus salarial."""

    print("\tExercício 1 - Bonus salario\n")

    salario = float(input("Digite o seu salário:"))
    tempo = int(input("Digite o tempo de empresa:"))

    salarioFinal = utils.CalculoBonusSalario(salario, tempo)

    print(f"O seu salário com o bônus é: R$ {salarioFinal:.2f}")



def exercicio02() -> None:
    """ Executa o exercício 2 - Identificador de triângulo."""

    print("\tExercício 2 - Identificador de triângulo\n")

    lado1 = float(input("Digite o comprimento do primeiro lado: "))
    lado2 = float(input("Digite o comprimento do segundo lado: "))
    lado3 = float(input("Digite o comprimento do terceiro lado: "))

    tipo_triangulo = utils.IdentificadorTriangulo(lado1, lado2, lado3)
    print(f"O triângulo é: {tipo_triangulo}")



def exercicio03() -> None:
    """ Executa o exercício 3 - Calculadora de IMC."""

    print("\tExercício 3 - Calculadora de IMC\n")

    peso = float(input("Digite o seu peso (kg): "))
    altura = float(input("Digite a sua altura (m): "))

    classificacao = utils.CalculadoraIMC(peso, altura)
    print(f"Sua classificação de IMC é: {classificacao}")
            


def exercicio04() -> None:
    """ Executa o exercício 4 - Cálculo de média."""

    print("\tExercício 4 - Calculo de média\n")

    notas = [0, 0, 0]

    for i in range(3):
        notas[i] = float(input(f"Digite a  {i+1}° nota: "))
        if(notas[i] == 0):
            break

    media = utils.CalculaMedia(notas)

    if(media >= 7):
        print("Aluno aprovado!")

    elif(media >= 5 and media < 7):
        print("Aluno em recuperação!")

    elif(media < 5):
        print("Aluno reprovado!")



def exercicio05() -> None:
    """" Executa o exercício 5 - Verificador de data válida."""

    print("\tExercício 5 - Verificador de data valida\n")

    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    if(utils.DataEhValida(dia, mes, ano)):
        print("Data válida!")

    else:
        print("Data inválida!")



def exercicio06() -> None:
    """" Executa o exercício 6 - Verificador de condição de voto."""

    idade = int(input("Digite sua idade: "))
    nacionalidade = input("Você é brasileiro(a)? (s/n) ").lower()

    if(idade >= 18):
        if(nacionalidade == 's'):
            print("Você deve votar!")
        else:
            print("Voto opcional.")
        
    elif(idade < 18 and idade >= 16):
        print("Voto opcional.")
    else:
        print("Não pode votar!")



def exercicio07() -> None:
    """ Executa o exercício 7 - Classificador de risco de renda."""

    print("\tExercício 7 - Classificador de risco\n")

    idade =  int(input("Digite sua idade: "))
    renda = float(input("Digite sua renda mensal: "))
    dividas = float(input("Digite o valor total de suas dívidas: "))

    classificacao = utils.ClassificadorRiscoRenda(renda, dividas, idade)
    print(f"Sua Classificação de risco é: {classificacao}")



def exercicio08() -> None:
    """ Executa o exercício 8 - Jogo da adivinhação."""

    print("\tExercício 8 - Jogo da adivinhação\n")

    cartasGab = ['B', 'C', 'D','A']
    
    cartas = input("Digite a sequência de 4 cartas:")
    cartas = cartas.upper()

    pontuacao = utils.CalculaPontuacao(cartas, cartasGab)

    print("A sequência de cartas era",cartasGab, "\n")
    print("Pontuação final:", pontuacao, "\n")



def exercicio09() -> None:
    """ Executa o exercício 9 - Desconto para cliente VIP."""

    print("\tExercício 9 - Desconto para cliente VIP\n")

    preco = float(input("Qual o preço do produto? R$ "))
    vip = input("O cliente é VIP? (S/N) ").upper()

    desconto = utils.CalculaDesconto(preco, vip)

    print(f"O valor do desconto é R$ {desconto:.2f}")



def exercicio10() -> None:
    """ Executa o exercício 10 - Validador de senha."""

    print("\tExercício 10 - Validador de senha\n")

    senha_invalida = True

    while(senha_invalida):
        senha = input("Digite a senha: ")
        if(len(senha) < 8):
            print("A senha deve conter no minimo 8 caracteres.")
        else:
            senha_invalida = False

    if(utils.SenhaEhForte(senha)):
        print("Sua senha é forte o suficiente!")
    else:
        print("Sua senha é fraca demais!")