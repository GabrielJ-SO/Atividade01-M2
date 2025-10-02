
import os
import utils
import exercicios

continuar = True

while continuar:
    os.system('cls')
    opcao = utils.menu()
     
    match opcao:
       
        case "1":
            
            exercicios.exercicio01()
            os.system('pause')
            continue

        case "2":
            
            exercicios.exercicio02()
            os.system('pause')
            continue

        case "3":

            exercicios.exercicio03()
            os.system('pause')
            continue

        case "4":

            exercicios.exercicio04()
            os.system('pause')
            continue

        case "5":

            exercicios.exercicio05()
            os.system('pause')
            continue

        case "6":
            
            exercicios.exercicio06()
            os.system('pause')
            continue

        case "7":

            exercicios.exercicio07()
            os.system('pause')
            continue
        
        case "8":


            continue

        case "9":


            continue

        case "10":


            continue

        case "0":
        
            print("Saindo...")
            continuar = False
            continue 

        case _:
            print("Opção inválida.")