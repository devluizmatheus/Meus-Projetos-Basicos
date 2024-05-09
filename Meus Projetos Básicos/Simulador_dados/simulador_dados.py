#Luiz Matheus de Olveira Leite 29/04/24
#Uma possível resolução para esse projeto de uma Lista de Contatos
#Esse Exercício foi postado no meu insta: @devluizmatheus
#Obs: Se houver algum erro ou dúvida pode avisar a mim no direct 

#Esse random é usado para mostrar valores aleatórias em um determinado campo
import random   


while True:
    #Menu principal do simulador
    inicio = input('▀▄▀▄▀▄🄳🄰🄳🄾🅂▀▄▀▄▀▄\nBem vindo a o simulador de dados! Deseja jogar:'
                    '\n[S]im\n[N]ão\n').upper()
    if inicio != 'S' and inicio != 'N':
        print('Escolha uma das opções')

    if inicio == 'N':
        print('Obrigado pela atenção')
        break
    if inicio == 'S':
        #Para quem não sabe esse try e except vai tentar processar o código até existir algum erro
        try:
            qtd_dados = int(input('Escolha quantos dados serão lançados: '))
            faces = int(input('Escolha quantas faces vai ter cada lado: '))
            for _ in range(qtd_dados):
                print(random.randint(1, faces))
                

        #O ValueError vai acontecer caso o usuário coloque um valor diferente do definido
        except ValueError:
            print('Digite um número válido')