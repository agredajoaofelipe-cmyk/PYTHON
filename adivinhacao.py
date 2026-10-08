import random

#numero_secreto = 11
#chute = int(input('Escolha umnumero entre 1 a 10: '))

#if chute > numero_secreto:
#    print('Voce errou! Tente um numero menor.')
#elif chute < numero_secreto:
#    print('Voce errou! Tente um numero maior')
#else:
#    print('Voce acertou!')   

numero_secreto = random.randint(1, 20)
tentativas = 0

print('Tente adivinhar o numero que estou pensando... entre 1 a 20')

for tentativas in range(1,6):
    chute = int(input('Seu palpite: '))

    if chute < numero_secreto:
       print('Voce errou! Tente um numero maior')
    elif chute > numero_secreto:
        print('Voce errou! Tente um numero menor')
    else:
        print( f'Acertou em {tentativas} tentativas(s)!') 
        break

else:
    print(f'Acabaram as tentativas. O numero era {numero_secreto}')

#while True:
#    chute = int(input('Seu palpite: '))
#    tentativas += 1

#    if chute < numero_secreto:
#       print('Voce errou! Tente um numero maior')
#    elif chute > numero_secreto:
#        print('Voce errou! Tente um numero menor')
#    else:
#        print( f'Acertou em {tentativas} tentativas(s)!') 
#        break           
 