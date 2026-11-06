import math
import random

#exercicio 16
print('Exercício 16 - Porção Inteira')
num = float(input('Digite um número real: '))
print(f'O número digitado foi {num}, seu valor inteiro é {math.trunc(num)}')
print('-' * 20)

#exercicio 17
print('Exercício 17 - Hipotenusa')
cateto_oposto = float(input('Digite o valor do comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')
print('-' * 20)

#exercicio 18
print('Exercício 18 - Seno, Cosseno e Tangente')
angulo = float(input('Digite o valor do angulo em graus: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O angulo é {angulo}°\nO seno é {seno:.2f}\nO cosseno é {cosseno:.1f}\nE a tangente é {tangente:.2f}')
print('-' * 20)

#exercicio 19
print('Exercício 19 - Sorteando em uma lista')
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
aleatorio = random.choice(lista)
print(f'O aluno escolhido foi {aleatorio} para apagar o quadro')
print('-' * 20)

#exercicio 20
print('Exercício 20 - Ordem de apresentação')
random.shuffle(lista)
print(f'A ordem de apresentação será: {lista}')
print('-' * 20)
