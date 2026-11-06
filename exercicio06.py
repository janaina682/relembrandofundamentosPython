#exercicio 28
import random
print('Exercício 28 - jogo da Advinhação')
numero_aleatorio = random.randint(0,5)
numero_usuario = int(input('Tente adivinhar qual numero eu escolhi entre 0 e 5: '))
if numero_usuario == numero_aleatorio:
    print(f'Parabéns! Você acertou, o número era {numero_aleatorio}')
else:
    print(f'Você errou! Eu escolhi o número {numero_aleatorio}')
print('-+' * 20)

#exercicio 29
print('Exercício 29 - Radar eletrônico')
velocidade = float(input('Digite a velocidade do carro em km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você está acima da velocidade permitida! Sua multa é de R$ {multa:.2f}')
else:
    print('Você está dentro da velocidade permitida! Tenha uma Boa viagem!')
print('-+' * 20)

#exercício 30
print('Exercício 30 - É par ou é impar? ')
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')
print('-+' * 20)

#exercicio 31
print('Exercício 31 - Custo da Viagem')
distancia = float(input("Digite a distância em quilometros: "))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'O preço da passagem é de R$ {preco:.2f}')
print('-+' * 20)
