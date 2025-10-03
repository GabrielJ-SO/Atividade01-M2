

def menu() -> None:
    """ Exibe o menu e retorna a opção selecionada.

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
    print(".7 - Classificador de risco de renda")
    print(".8 - Jogo de adivinhação")
    print(".9 - Desconto para cliente VIP")
    print(".10 - Validador de senha")
    print(".0 - Sair")
    opcao = str(input("Digite a opção desejada: "))

    return opcao



def CalculoBonusSalario(salario, tempo) -> float:
    """ Calcula o bônus salarial com base no salário e tempo de empresa.
    
    Args:
        salario (float): Salário atual do funcionário.
        tempo (int): Tempo de empresa em anos.

    Returns:
        float: Salário final com o bônus aplicado.
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
    """ Identifica o tipo de triângulo com base nos comprimentos dos lados.
    
    Args:
        lado1 (float): Comprimento do primeiro lado.
        lado2 (float): Comprimento do segundo lado.
        lado3 (float): Comprimento do terceiro lado.

    Returns:
        str: Tipo de triângulo ("Equilátero", "Isósceles", "Escaleno" ou "Não é um triângulo").
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
    """ Calcula o Índice de Massa Corporal (IMC) e classifica o resultado.
    
        Args:
            peso (float): Peso em quilogramas.
            altura (float): Altura em metros.

        Returns:
            str: Classificação do IMC.
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
    """ Calcula a média de uma lista de notas.
    
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



def DataEhValida(dia, mes, ano) -> bool:
    """ Verifica se uma data é válida.
    
        Args:
            dia (int): Dia do mês.
            mes (int): Mês.
            ano (int): Ano.

        Returns:
            bool: True se a data for válida, False caso contrário.
    """

    if(ano < 0):
        return False

    elif(mes < 1 or mes > 12):
        return False

    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia < 1 or dia > 30):
            return False
        else:
            return True

    elif(mes == 2):
        if(ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
            if(dia < 1 or dia > 29):
                return False
            else:
                return True
        else:
            if(dia < 1 or dia > 28):
                return False
            else:
                return True

    else:
        if(dia < 1 or dia > 31):
            return False
        else:
            return True
        


def ClassificadorRiscoRenda(renda, dividas, idade) -> str:
    """" Classifica o risco de crédito com base na renda, dívidas e idade.
    
        Args:
            renda (float): Renda mensal
            dividas (float): Valor total de dívidas mensais
            idade (int): Idade do usuário
            
        Returns:
            str: Classificação de risco ("Baixo", "Médio", "Alto" ou "Médio-baixo")"""
    
    if(renda >= 5000 and dividas < (renda * 0.3)):
        return "Baixo"
    elif(renda <= 5000 and dividas <= (renda * 0.5)):
        return "Médio"
    elif(renda < 2000  and dividas > (renda * 0.5)):
        return "Alto"
    else:
        return "Médio-baixo"



def CalculaPontuacao(cartas, cartasGab) -> int:
    """ Calcula a pontuação do jogador com base nas cartas escolhidas.
    
        Args:
            cartas (str): Sequência de cartas escolhidas pelo jogador.
            cartasGab (list of str): Sequência correta de cartas.

        Returns:
            int: Pontuação final do jogador.
    """

    pontuacao = 0

    if "CD" in cartas:
        pontuacao += 5
    
    i = 0
    for carta in cartas:
        if carta == cartasGab[i]:
            pontuacao += 10

        if carta == 'A':
            pontuacao += 5

        i += 1

    return pontuacao



def CalculaDesconto(preco, vip) -> float:
    """ Calcula o desconto para clientes VIP com base no preço do produto.
    
        Args:
            preco (float): Preço do produto.
            vip (str): Indica se o cliente é VIP ('S' para sim, 'N' para não).

        Returns:
            float: Valor do desconto aplicado.
    """

    if(preco >= 100):
        if(vip == 'S'):
            desconto = preco * 0.25
        else:
            desconto = preco * 0.20
    elif(preco >= 50):
        if(vip == 'S'):
            desconto = preco * 0.15
        else:
            desconto = preco * 0.10
    elif(preco < 50):
        if(vip == 'S'):
            desconto = preco * 0.05
        else:
            desconto = 0

    return desconto



def SenhaEhForte(senha) -> bool:
    """ Verifica a segurança da senha.
    
        Args:
            senha (str): Senha a ser verificada.

        Returns:
            bool: True se a senha for forte, False caso contrário.
    """

    senha_forte = False
    tem_especial = False
    tem_numero = False
    tem_lower = False
    tem_upper = False
    especiais =  ['!', '@', '#', '$', '%']

    for char in senha:

        if char.isdigit():
            tem_numero = True
        if char.islower():
            tem_lower = True
        if char.isupper():
            tem_upper = True

    for especial in especiais:
        if(especial in senha):
            tem_especial = True
            break

    if(tem_numero and tem_lower and tem_upper and tem_especial):
        senha_forte = True

    return senha_forte