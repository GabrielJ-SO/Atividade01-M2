
import os
import utils
import exercicios

opcaoExercicios = {
                    "1": exercicios.exercicio01,
                    "2": exercicios.exercicio02, 
                    "3": exercicios.exercicio03,
                    "4": exercicios.exercicio04, 
                    "5": exercicios.exercicio05, 
                    "6": exercicios.exercicio06, 
                    "7": exercicios.exercicio07, 
                    "8": exercicios.exercicio08, 
                    "9": exercicios.exercicio09, 
                    "10": exercicios.exercicio10
                    }

while True:
    os.system('cls')

    opcao = utils.menu()
    
    if opcao == "0":
        print("Saindo...")
        break

    if opcao in opcaoExercicios:
        os.system('cls')
        opcaoExercicios[opcao]()
        os.system('pause')

    else:
        print("Opção inválida.")
        os.system('pause')
    