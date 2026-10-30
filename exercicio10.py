from time import sleep
#exercicio 46
print('Exercício 46 - contagem regressiva')
print('Vai começar a contagem para os fogos...')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('******** FOGOS ******')
print('*/*' * 20)

#exercicio 47
print('Exercicio 47 - Números pares entre 1 e 50')

for n in range(2, 51, 2):
    print(n, end=' ')
print('\n')
print('*/*' * 20)

#exercicio 48
print('Exercicio 48 - Soma dos números impares, multiplos de 3, entre 1 e 500')
soma = 0
for numero in range(0, 500, 3):
    if numero % 2 != 0:
        soma += numero
print(soma)
print('*/*' * 20)

#exercicio 49
print('Exercicio 49 - Tabuada')
numero = int(input('Digite um número para gerar a tabuada dele: '))
print('A tabuada de {} é:'.format(numero))

for n in range(0, 11):
    print('{} x {} = {}'.format(numero, n, numero * n))
print('*/*' * 20)

#exercicio 50
print('Exercicio 50 - Ler números e retornar soma apenas dos pares')
soma = 0
for n in range(0,6):
    n = int(input('Digite um número para a soma '))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares que você digitou da: {} '.format(soma))