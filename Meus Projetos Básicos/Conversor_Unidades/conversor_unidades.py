#Luiz Matheus de Olveira Leite 29/04/24
#Uma possível resolução para esse projeto de conversor de unidades
#Esse Exercício foi postado no meu insta: @devluizmatheus
#Obs: Se houver algum erro ou dúvida pode avisar a mim no direct 

#Usado para usar o os.system('cls') e da um clear no terminar
import os 


while True:
    #Menu principal do conversor
    print('Temperatura\n[A]: °F-°C\n[B]: °C-°F \n[C]: K-°C\n[D]: °C-K')   
            
            
    conversão = input('Escolha o tipo de conversão: ').upper()
    os.system('cls')

    if conversão == 'A':
        os.system('cls')
        #Para quem não sabe esse try e except vai tentar processar o código até existir algum erro
        try:
            tc = float(input('Escolha uma temperatura em °F para converter °C: '))
            if tc:
                print(tc - 32/1.8)
            else:
                print('Digite na escala de 0 a 100')
        #O ValueError vai acontecer caso o usuário coloque um valor diferente do definido
        except ValueError:
            print('Insira o valor da temperatura.')
    elif conversão  == 'B':
        os.system('cls')
        try:
            tf = float(input('Escolha uma temperatura em °C para converter °F: '))
            if tf:
                print(1.8*tf + 32)
        except ValueError:
            print('Insira o valor da temperatura.')

    if conversão == 'C':
        os.system('cls')
        try:
            tck = float(input('Escolha uma temperatura em K para °C: '))
            if tck:
                print(tck - 273)
        except ValueError:
            print('Insira o valor da temperatura.')

    if conversão == 'D':
        os.system('cls')
        try:
            tkc = float(input('Escolha uma temperatura em °C para K: '))
            if tkc:
                print(tkc + 273)
        except ValueError:
            print('Insira o valor da temperatura.')