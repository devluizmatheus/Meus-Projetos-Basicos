#Luiz Matheus de Olveira Leite 29/04/24
#Uma possível resolução para esse projeto de conversor de unidades
#Esse Exercício foi postado no meu insta: @devluizmatheus
#Obs: Se houver algum erro ou dúvida pode avisar a mim no direct 

while True:
    try:
        av1 = float(input('Digite Av1: '))
        av2 = float(input('Digite Av2: '))
        av3 = float(input('Digite Av3: '))
        media = av1, av2, av3
        print('Média: ', sum(media)/ len(media))
    except ValueError:
        print('Digite apenas um número')