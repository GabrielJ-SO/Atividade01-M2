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

            utils.CalculoBonusSalario(salario, tempo)
            
            input("Pressione Enter para continuar...")
            continue
        case "2":
            print("Exercício 2 - identificador de triângulo")
            continue
        case "10":
            print("Exercício 10 - Validador de senha")
            continue
        case "0":
            print("Saindo...")
            continuar = False
            continue 
        case _:
            print("Opção inválida.")