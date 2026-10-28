#exercicio 28
import random
print('Exercício 28 - jogo da Advinhação')
numero_aleatorio = random.randint(0,5)
numero_usuario = int(input('Tente adivinhar qual numero eu escolhi entre 0 e 5: '))
if numero_usuario == numero_aleatorio:
    print('Parabéns! Você acertou, o número era {}'.format(numero_aleatorio))
else:
    print('Você errou! Eu escolhi o número {}'.format(numero_aleatorio))
print('-+' * 20)

#exercicio 29
print('Exercício 29 - Radar eletrônico')
velocidade = float(input('Digite a velocidade do carro em km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você está acima da velocidade permitida! Sua multa é de R${:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade permitida! Tenha uma Boa viagem!')
print('-+' * 20)

#exercício 30
print('Exercício 30 - É par ou é impar? ')
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))
print('-+' * 20)

#exercicio 31
print('Exercício 31 - Custo da Viagem')
distancia = float(input("Digite a distância em quilometros: "))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('O preço da passagem é de R${:.2f}'.format(preco))
print('-+' * 20)
