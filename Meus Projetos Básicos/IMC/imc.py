#Luiz Matheus de Olveira Leite 29/04/24
#Uma possível resolução para esse projeto de uma Lista de Contatos
#Esse Exercício foi postado no meu insta: @devluizmatheus
#Obs: Se houver algum erro ou dúvida pode avisar a mim no direct 

while True:
    try:
        peso = float(input('Informe seu peso(em quilos): '))
        altura = float(input('Informe sua Altura(Metros): '))
        
        imc = peso/ altura**2
    except ValueError:
        print('Digite apenas números!!')

    if imc < 18.5:
        print('Você está abaixo do peso')
    
    elif imc > 18.6 and imc < 24.9:
        print('Peso ideial Parabéns!! :D')
    
    elif imc > 25 and imc < 29.9:
        print('Levemente acima do peso')
    
    elif imc > 30 and imc < 34.9:
        print('Obesidade Grau 1')

    elif imc > 35 and imc < 39.9:
        print('Obesidade Grau 2 (severa)') 

    elif imc > 40:
        print('Obesidade Grau 3 (mórbita)')
    
    

    