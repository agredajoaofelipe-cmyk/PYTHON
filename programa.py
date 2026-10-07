nome = "Joao"
idade = 18
altura = 1.85
print(f'Meu nome e {nome}, tenho {idade} anos e {altura} de altura')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seo peso: '))
imc = peso / altura ** 2
print(f'Meu nome e {nome}, tenho {idade} anos e {altura} de altura. Meu peso e {peso}. IMC: {imc:.2f}')