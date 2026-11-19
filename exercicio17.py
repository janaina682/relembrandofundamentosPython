'''
#exercicio 72
print('Exercicio 72 - aprendendo Tuplas')
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num < 0 or num >20:
        print('O número tem que estar entre 0 e 20. Tente novamente')
    else:
        break
print(f'Você digitou o número {numeros[num]}')
print('*-' * 20)

#exercicio 73
print('Exercicio 73 - Usando Tuplas')
times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Fluminense', 'Athletico-PR', 'Bahia', 'Atlético-MG', 'Santos', 'Bragantino', 'São Paulo', 'Vasco da Gama', 'Botafogo', 'Coritiba', 'Mirassol', 'Corinthians', 'EC Vitória', 'Internacional', 'Grêmio', 'Remo', 'Chapecoence')
print(times)
print('-'*20)
print('Os primeiros 5 colocados na tabela são:')
for a in range(5):
    print(f'{a+1}° Colocado: {times[a]}')
print('-'*20)
print('Os quatro útimos na tabela são: ')
for b in range(19, 15, -1):
    print(f'{b+1}° Colocado {times[b]}')
print('-'*20)
print('A lista dos times em ordem alfabética')
times_ordem = sorted(times)
for c in times_ordem:
    print(c)
print('-'*20)
chapeco = times.index('Chapecoence')+1
print(f'O Chapecoense está na {chapeco}° posição')
print('*-' * 20)
#exercicio 74
print('Exercicio 74 - números aleatórios e tuplas')
import random
numeros = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10), random.randint(0,10)) 
print(f'Foram sorteados os números: {numeros} ')
maior = menor = cont = 0
for i in numeros:
    if i > maior:
        maior = i
    if cont == 0:
        menor = i 
    cont += 1
    if i < menor:
        menor = i
print(f'O maior número sorteado foi: {maior}')
print(f'O menor número sorteado foi: {menor}')
print('*-' * 20)
#exercicio 75
print('Exercicio 75 - input de dados armazenados numa tupla')
valores = int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: '))
print(f'Você digitou os valores: {valores}')
print(f'O número 9 apareceu: {valores.count(9)} vezes')
for posicao, i in enumerate(valores):
    if i == 3:
            print(f'O número 3 foi digitado na posição: {posicao +1}')
if valores.count(3) == 0:
    print('Não foi digitado nenhum número "3"')
print('Os valores pares digitados foram: '.format(),end=' ')
for v in valores:
        if v % 2 == 0:
            print('{}'.format(v), end = ' ')
print('*-' * 20)
'''

