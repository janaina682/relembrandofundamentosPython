
#exercicio 72
print('Exercicio 72 - aprendendo Tuplas')
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Desesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if num < 0 or num >20:
            print('O número tem que estar entre 0 e 20. Tente novamente')
        else:
            break
    print(f'Você digitou o número {numeros[num]}')
    contunuar = input('Quer continuar? [S/N]').upper()
    if contunuar == 'N':
        break
print('*-' * 20)

#exercicio 73
print('Exercicio 73 - Usando Tuplas')
times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Fluminense', 'Athletico-PR', 'Bahia', 
         'Atlético-MG', 'Santos', 'Bragantino', 'São Paulo', 'Vasco da Gama', 'Botafogo', 
         'Coritiba', 'Mirassol', 'Corinthians', 'EC Vitória', 'Internacional', 'Grêmio',
         'Remo', 'Chapecoence')
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
numeros = (random.randint(0,10),
           random.randint(0,10),
           random.randint(0,10),
           random.randint(0,10),
           random.randint(0,10)) 
print(f'Foram sorteados os números: {numeros} ')
'''maior = menor = cont = 0
for i in numeros:
    if i > maior:
        maior = i
    if cont == 0:
        menor = i 
    cont += 1
    if i < menor:
        menor = i'''
print(f'O maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')
print('*-' * 20)
#exercicio 75
print('Exercicio 75 - input de dados armazenados numa tupla')
valores = (int(input('Digite um número: ')),
           int(input('Digite um número: ')), 
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os valores: {valores}')
print(f'O número 9 apareceu: {valores.count(9)} vezes')
'''for posicao, i in enumerate(valores):
    if i == 3:
            print(f'O número 3 foi digitado na posição: {posicao +1}')
'''

if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}° posição')
else:
    print('Não foi digitado nenhum número "3"')
print('Os valores pares digitados foram: '.format(),end=' ')
for v in valores:
        if v % 2 == 0:
            print('{}'.format(v), end = ' ')
print('\n')
print('*-' * 20)

#Exercicio 76
print('Exercicio 76 - tupla de produtos')
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'* 40)
print('{: ^40}'.format(' LISTAGEM DE PREÇOS '))
print('-'* 40)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}',end='')
    else:
        print(f'R$: {listagem[posicao]:>6.2f}')
print('*-' * 20)
#exercicio 77
print('Exercicio 77 - Destrinchanto tuplas')
palavras = ('aprender', 'programar', 'linguagem', 'pyhton', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos: ',end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra} ',end='')
    print('')
print('*-' * 20)