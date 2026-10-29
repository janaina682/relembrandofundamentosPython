import time
#exercicio 46
print('Exercício 46 - contagem regressiva')
print('Vai começar a contagem para os fogos...')

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print('******** FOGOS ******')
print('*/*' * 20)
#exercicio 47
print('Exercicio 47 - Números pares entre 1 e 50')

for n in range(2, 51, 2):
    print(n)
print('*/*' * 20)


#exercicio 48
print('Exercicio 48 - Soma dos números impares, multiplos de 3, entre 1 e 500')
soma = 0
for numero in range(0, 500, 3):
    if numero % 2 != 0:
        soma += numero
print(soma)
print('*/*' * 20)
