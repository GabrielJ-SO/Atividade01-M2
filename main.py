import utils
import os

continuar = True

while continuar:
    os.system('cls')
    opcao = utils.menu()
     
    match opcao:
       
            
        case "1":

            print("\tExercício 1 - Bonus salario\n")

            salario = float(input("Digite o seu salário:"))
            tempo = int(input("Digite o tempo de empresa:"))

            salarioFinal = utils.CalculoBonusSalario(salario, tempo)

            print(f"O seu salário com o bônus é: R$ {salarioFinal:.2f}")
            
            input("Pressione Enter para continuar...")
            continue

        case "2":
            
            print("\tExercício 2 - Identificador de triângulo\n")

            lado1 = float(input("Digite o comprimento do primeiro lado: "))
            lado2 = float(input("Digite o comprimento do segundo lado: "))
            lado3 = float(input("Digite o comprimento do terceiro lado: "))

            tipo_triangulo = utils.IdentificadorTriangulo(lado1, lado2, lado3)
            print(f"O triângulo é: {tipo_triangulo}")

            input("Pressione Enter para continuar...")
            continue

        case "3":

            print("\tExercício 3 - Calculadora de IMC\n")

            peso = float(input("Digite o seu peso (kg): "))
            altura = float(input("Digite a sua altura (m): "))

            classificacao = utils.CalculadoraIMC(peso, altura)
            print(f"Sua classificação de IMC é: {classificacao}")

            input("Pressione Enter para continuar...")
            continue

        case "4":

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

            input("Pressione Enter para continuar...")
            continue

        case "5":

            print("\tExercício 5 - Verificador de data valida\n")



            input("Pressione Enter para continuar...")
            continue

        case "6":
            print("\tExercício 6 - Verifica condição de voto\n")



            input("Pressione Enter para continuar...")
            continue

        case "7":

            print("\tExercício 7 - Classificador de risco\n")



            input("Pressione Enter para continuar...")
            continue
        
        case "8":

            print("\tExercício 8 - Jogo de adivinhação\n")



            input("Pressione Enter para continuar...")
            continue

        case "9":

            print("\tExercício 9 - Desconto para cliente VIP\n")



            input("Pressione Enter para continuar...")
            continue

        case "10":

            print("\tExercício 10 - Validador de senha\n")

            continue
        case "0":
            print("Saindo...")
            continuar = False
            continue 
        case _:
            print("Opção inválida.")