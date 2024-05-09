#Luiz Matheus de Olveira Leite 29/04/24
#Uma possível resolução para esse projeto de uma Lista de Contatos
#Esse Exercício foi postado no meu insta: @devluizmatheus
#Obs: Se houver algum erro ou dúvida pode avisar a mim no direct 

#Usado para usar o os.system('cls') e da um clear no terminar
import os 

#Armazenamento de Contatos
contatos = []


while True:
    
    #O Menu principal do Código
    inicio = input('Agenda de Contatos \n[L]ista \n[A]dicionar \n[D]eletar  \nSelecione un para continuar: ').upper()
    #Caso o usuário não utilize uma das opções
    if inicio != 'L' and inicio != 'A' and inicio != 'D':
        print('Digite apenas uma das opções.')
        continue
    #Para listar o Número de elementos na lista
    if inicio == 'L':
        os.system('cls')
        for indice, elemento in enumerate(contatos):
            print(f'===========================\n'
                  f'Indice:{indice}\nContato: {nome} \nTelefone: {numero} \nEmail: {email}\n'
                '===========================')
                  
    #Para Adicionar os Elementos da lista
    if inicio == 'A':
        os.system('cls')
        nome = input('Adicione um nome: ')
        numero = input('Adicione um número de Telefone: ')
        email = input('Adicione um Email: ')
        adicionar = nome, numero, email
        contatos.append(adicionar)

    #Para deletar um indice na lista
    if inicio == 'D':
        #Para quem não sabe esse try e except vai tentar processar o código até existir algum erro
        try:
            os.system('cls')
            deletar = int(input('Qual é o indice do contato que deseja excluir? '))
            if 0 <= indice < len(contatos):
                del contatos[deletar]
        #O ValueError vai acontecer caso o usuário coloque um valor diferente do definido
        #E no IndexError é para caso o Usuário digite um indice fora da lista
        except ValueError: 
            print('Escolha apenas indices válidos!!')
        except IndexError:
            print('Escolha apenas indices válidos!!')
        else:
            print('Digite um indice válido')