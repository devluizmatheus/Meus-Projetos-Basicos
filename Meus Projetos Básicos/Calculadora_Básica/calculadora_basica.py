#Luiz Matheus de Olveira Leite 29/04/24
#Uma possível resolução para esse projeto de Calculadora Básica
#Esse Exercício foi postado no meu insta: @devluizmatheus
#Obs: Se houver algum erro ou dúvida pode avisar a mim no direct 

while True:
    #Menu principal da caluladora
    #Para quem não sabe esse try e except vai tentar processar o código até existir algum erro
    try:
        entrada = float(input('Digite um número: '))
        entrada_2 = input('Digite um Operador (+-*/): ')
        entrada_3 = float(input('Digite outro número: '))
        
        #Caso o Usuário nao digite nenhum dos operadores definidos
        if entrada_2 not in '+-*/':
            print('Digite um operador válido (+, -, *, /)')
        else:
            if entrada_2 == '+':
                print(entrada + entrada_3)
            elif entrada_2 == '-':
                print(entrada - entrada_3)
            elif entrada_2 == '*':
                print(entrada * entrada_3)
            elif entrada_2 == '/':
                if entrada_3 != 0:
                    print(entrada / entrada_3)
                else:
                    print("Não é possível dividir por zero.")
                    continue  
    #O ValueError vai acontecer caso o usuário coloque um valor diferente do definido
    except ValueError:
        print("Por favor, digite um número válido.")