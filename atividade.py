#1 - MOSTRE A TABUADA DE UM NUMERO ESCOLHIDA PELO USUARIO (1 A 10)
num = int(input('Tabuala do: '))
for tabuada in range(1, 11):
    print(f'{num} x {tabuada}  = {num * tabuada} ')
#2 - SOME TODOS OS NUMROS DE 1 A 100 USANDO FOR
soma = 0
for i in range(1, 101):
    soma += 1 
print(soma)    
#3 - FAÇA UMA CONTAGEM REGRESSIVA DE 10 ATE 1 E NO FIM MOSTRE "FOGO"
cont = 10
for e in range (1):
    const -= e
    print(cont)    
    print("FOGO!!!")
# 4 - PEÇA UMA SENHA REPETIDAMENTE ATE O USUARIO DIGITAL "python123"
 
senha = ''

while senha != 'python123':
    senha = input('Digite a senha correta: ')
print('Acesso liberado!')    